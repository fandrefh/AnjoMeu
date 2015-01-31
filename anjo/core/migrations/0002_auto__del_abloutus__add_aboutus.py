# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'AbloutUs'
        db.delete_table(u'core_abloutus')

        # Adding model 'AboutUs'
        db.create_table(u'core_aboutus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('about_us', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['AboutUs'])


    def backwards(self, orm):
        # Adding model 'AbloutUs'
        db.create_table(u'core_abloutus', (
            ('about_us', self.gf('django.db.models.fields.TextField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=70)),
        ))
        db.send_create_signal(u'core', ['AbloutUs'])

        # Deleting model 'AboutUs'
        db.delete_table(u'core_aboutus')


    models = {
        u'core.aboutus': {
            'Meta': {'object_name': 'AboutUs'},
            'about_us': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        }
    }

    complete_apps = ['core']