# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HowItWork'
        db.create_table(u'core_howitwork', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('how_work', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['HowItWork'])


    def backwards(self, orm):
        # Deleting model 'HowItWork'
        db.delete_table(u'core_howitwork')


    models = {
        u'core.aboutus': {
            'Meta': {'object_name': 'AboutUs'},
            'about_us': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        },
        u'core.howitwork': {
            'Meta': {'object_name': 'HowItWork'},
            'how_work': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        }
    }

    complete_apps = ['core']