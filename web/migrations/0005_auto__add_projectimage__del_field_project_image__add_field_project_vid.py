# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProjectImage'
        db.create_table('web_projectimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('altText', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('projectId', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Project'])),
        ))
        db.send_create_signal('web', ['ProjectImage'])

        # Deleting field 'Project.image'
        db.delete_column('web_project', 'image')

        # Adding field 'Project.video'
        db.add_column('web_project', 'video',
                      self.gf('django.db.models.fields.URLField')(default=None, max_length=200),
                      keep_default=False)

        # Adding field 'Project.url'
        db.add_column('web_project', 'url',
                      self.gf('django.db.models.fields.URLField')(default=None, max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'ProjectImage'
        db.delete_table('web_projectimage')

        # Adding field 'Project.image'
        db.add_column('web_project', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100),
                      keep_default=False)

        # Deleting field 'Project.video'
        db.delete_column('web_project', 'video')

        # Deleting field 'Project.url'
        db.delete_column('web_project', 'url')


    models = {
        'web.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'web.project': {
            'Meta': {'object_name': 'Project'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['web.Category']", 'symmetrical': 'False', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'thumbImage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'video': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'web.projectimage': {
            'Meta': {'object_name': 'ProjectImage'},
            'altText': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'projectId': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Project']"})
        }
    }

    complete_apps = ['web']