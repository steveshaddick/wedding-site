# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WeddingRSVP'
        db.create_table(u'wedding_rsvp_weddingrsvp', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('names', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('attending', self.gf('django.db.models.fields.BooleanField')()),
            ('dietary_restrictions', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'wedding_rsvp', ['WeddingRSVP'])


    def backwards(self, orm):
        # Deleting model 'WeddingRSVP'
        db.delete_table(u'wedding_rsvp_weddingrsvp')


    models = {
        u'wedding_rsvp.weddingrsvp': {
            'Meta': {'object_name': 'WeddingRSVP'},
            'attending': ('django.db.models.fields.BooleanField', [], {}),
            'dietary_restrictions': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'names': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['wedding_rsvp']