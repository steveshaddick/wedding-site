require 'capistrano/ext/multistage'
require File.expand_path(File.dirname(__FILE__) + '/functions')

set :stages, %w(production)

set :deploy_via, :remote_cache
set :use_sudo, false
set :keep_releases, 5
set :normalize_asset_timestamps, false

set :scm, :git
set :repository, "https://github.com/steveshaddick/wedding-site.git"

set :local_data_dir, File.expand_path(File.dirname(__FILE__) + "/../data")
set :python_virtualenv, "melissasteveenv"
set :django_project, "melissa_steve"
set :grunt_tasks, ['production']


default_run_options[:pty] = true
default_run_options[:shell] = false
ssh_options[:forward_agent] = true


#############################################################
#   Tasks
#############################################################
 
#after :deploy, 'deploy:cleanup'
after "deploy:update", "env:move"

namespace :deploy do
  task :cold do
    setup
    update
    env:move
  end

  task:restart, :except => { :no_release => true } do
    #supervisor must be set up
    #(bit of a mistake in the in the configs)
    if environment == 'production'
      sudo "uwsgi --reload /tmp/melissasteve.pid"
    end
  end

  task :start do
    #sudo "uwsgi --reload #{pidfile}"
  end

end


namespace :env do

  task :move do
    env_path = File.expand_path(File.dirname(__FILE__) + "/environments/#{environment}")
    upload("#{env_path}/settings.py","#{release_path}/melissa_steve/settings/env.py")
    upload("#{env_path}/robots.txt","#{release_path}/melissa_steve/melissa_steve/templates/melissa_steve/robots.txt")
  end

end


namespace :data do

  task :backup do

    t = Time.new
    run "mkdir -p #{data_dir}/bu"
    run_locally "mkdir -p #{local_data_dir}/#{environment}/bu"

    run "source #{shared_path}/#{python_virtualenv}/bin/activate && cd #{current_release}/#{django_project} && python manage.py dumpdata --natural > #{data_dir}/data.json && deactivate"
    run "cp #{data_dir}/data.json #{data_dir}/bu/"+ t.strftime("%Y%m%d_%H%M%S") + "_data.json"

    download("#{data_dir}/data.json", "#{local_data_dir}/#{environment}/data.json", :via => :scp)
    run_locally "cp #{local_data_dir}/#{environment}/data.json #{local_data_dir}/#{environment}/bu/"+ t.strftime("%Y%m%d_%H%M%S") + "_data.json"
  end


  task :set do
    backup

    upload("#{local_data_dir}/#{environment}/data.json", "#{data_dir}/data.json", :via => :scp)

    drop_tables_bash = "echo 'show tables;'     | python manage.py dbshell     | sed -n 2,\\$p     | awk 'BEGIN {print \"set foreign_key_checks=0;\"} { print \"drop table `\" $1 \"`;\"}'     | python manage.py dbshell"
    run "source #{shared_path}/#{python_virtualenv}/bin/activate && cd #{current_release}/#{django_project} && #{drop_tables_bash} && deactivate"
    run "source #{shared_path}/#{python_virtualenv}/bin/activate && cd #{current_release}/#{django_project} && python manage.py syncdb --migrate --noinput && python manage.py loaddata #{data_dir}/data.json && deactivate"
  end


  task :sync do
    run "source #{shared_path}/#{python_virtualenv}/bin/activate && cd #{current_release}/#{django_project} && python manage.py syncdb --migrate --noinput && deactivate"
  end


  task :clean_backups do
    run "find #{data_dir}/bu/ -type f -mtime +3 -exec rm {} \\;"
  end
end
