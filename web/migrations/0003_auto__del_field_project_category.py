# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Project.category'
        db.delete_column('web_project', 'category_id')

        # Adding M2M table for field category on 'Project'
        db.create_table('web_project_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['web.project'], null=False)),
            ('category', models.ForeignKey(orm['web.category'], null=False))
        ))
        db.create_unique('web_project_category', ['project_id', 'category_id'])


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Project.category'
        raise RuntimeError("Cannot reverse this migration. 'Project.category' and its values cannot be restored.")
        # Removing M2M table for field category on 'Project'
        db.delete_table('web_project_category')


    models = {
        'web.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'web.project': {
            'Meta': {'object_name': 'Project'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['web.Category']", 'symmetrical': 'False', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'thumbImage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['web']