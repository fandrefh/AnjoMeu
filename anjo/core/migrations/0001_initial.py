# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AbloutUs'
        db.create_table(u'core_abloutus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('about_us', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['AbloutUs'])


    def backwards(self, orm):
        # Deleting model 'AbloutUs'
        db.delete_table(u'core_abloutus')


    models = {
        u'core.abloutus': {
            'Meta': {'object_name': 'AbloutUs'},
            'about_us': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        }
    }

    complete_apps = ['core']