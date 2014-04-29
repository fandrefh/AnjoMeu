# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Campaign.photo'
        db.alter_column(u'campaign_campaign', 'photo', self.gf('cloudinary.models.CloudinaryField')(max_length=100))

    def backwards(self, orm):

        # Changing field 'Campaign.photo'
        db.alter_column(u'campaign_campaign', 'photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

    models = {
        u'campaign.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'goal': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'photo': ('cloudinary.models.CloudinaryField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['campaign']