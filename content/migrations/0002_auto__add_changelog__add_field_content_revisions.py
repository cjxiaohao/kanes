# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Changelog'
        db.create_table('content_changelog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['content.Content'])),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('additions', self.gf('django.db.models.fields.IntegerField')()),
            ('deletions', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('content', ['Changelog'])

        # Adding field 'Content.revisions'
        db.add_column('content_content', 'revisions',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Changelog'
        db.delete_table('content_changelog')

        # Deleting field 'Content.revisions'
        db.delete_column('content_content', 'revisions')


    models = {
        'content.changelog': {
            'Meta': {'object_name': 'Changelog'},
            'additions': ('django.db.models.fields.IntegerField', [], {}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'content': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['content.Content']"}),
            'deletions': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'content.content': {
            'Meta': {'object_name': 'Content'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'revisions': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['content']