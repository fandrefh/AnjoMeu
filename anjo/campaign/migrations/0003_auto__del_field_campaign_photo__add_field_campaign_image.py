# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Campaign.photo'
        db.delete_column(u'campaign_campaign', 'photo')

        # Adding field 'Campaign.image'
        db.add_column(u'campaign_campaign', 'image',
                      self.gf('cloudinary.models.CloudinaryField')(default=0, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Campaign.photo'
        db.add_column(u'campaign_campaign', 'photo',
                      self.gf('cloudinary.models.CloudinaryField')(default=0, max_length=100),
                      keep_default=False)

        # Deleting field 'Campaign.image'
        db.delete_column(u'campaign_campaign', 'image')


    models = {
        u'campaign.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'goal': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('cloudinary.models.CloudinaryField', [], {'max_length': '100'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['campaign']