############################################################
#   Functions
############################################################
def remote_symlink_exists?(full_path)
  'true' == capture("if [ -L #{full_path} ]; then echo 'true'; fi").strip
end

def remote_file_exists?(full_path)
  'true' == capture("if [ -f #{full_path} ]; then echo 'true'; fi").strip
end

def remote_dir_exists?(full_path)
  'true' == capture("if [ -d #{full_path} ]; then echo 'true'; fi").strip
end