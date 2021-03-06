from django.contrib import admin
from models import *

def question_part(obj):
    return obj.question[:250]

class QuestionAdmin(admin.ModelAdmin):
    list_display=('pk', 'published', question_part, 'answer', 'difficulty')
    list_filter=('published', 'difficulty')
    search_fields=('question', 'explanation')

class UsersAnswerAdmin(admin.ModelAdmin):
    list_display=('question', 'result', 'answer', 'correct', 'ip', 'date_time')
    list_filter=('question',)

class QuizAdmin(admin.ModelAdmin):
    list_display=('key', 'date_time', 'question_ids')
    search_fields=('key',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(UsersAnswer, UsersAnswerAdmin)
admin.site.register(Quiz, QuizAdmin)
