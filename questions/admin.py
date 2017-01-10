from django.contrib import admin
from .models import Question, Answers ,Correct
# Register your models here.
admin.site.register(Question)
admin.site.register(Answers)
admin.site.register(Correct)