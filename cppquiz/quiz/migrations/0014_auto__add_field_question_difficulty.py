# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Question.difficulty'
        db.add_column('quiz_question', 'difficulty',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Question.difficulty'
        db.delete_column('quiz_question', 'difficulty')


    models = {
        'quiz.question': {
            'Meta': {'object_name': 'Question'},
            'answer': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'author_email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '254', 'blank': 'True'}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'difficulty': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'explanation': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'result': ('django.db.models.fields.CharField', [], {'default': "'OK'", 'max_length': '2'})
        },
        'quiz.usersanswer': {
            'Meta': {'object_name': 'UsersAnswer'},
            'answer': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'correct': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '45', 'blank': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quiz.Question']"}),
            'result': ('django.db.models.fields.CharField', [], {'default': "'OK'", 'max_length': '2'})
        }
    }

    complete_apps = ['quiz']