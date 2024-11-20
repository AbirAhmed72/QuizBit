from django.contrib import admin
from .models import AnswerChoice, Question, PracticeHistory
# Register your models here.

admin.site.register(Question)
admin.site.register(PracticeHistory)
admin.site.register(AnswerChoice)