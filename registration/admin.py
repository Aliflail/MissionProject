from django.contrib import admin
from .models import Profile,Tests,Question,Choice,Correct,Testscore
# Register your models here.
admin.site.register(Profile)
admin.site.register(Tests)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Correct)
admin.site.register(Testscore)
