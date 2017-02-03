from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL)
    admissionno=models.IntegerField()
    choice = (
        ('PC', 'Placement_Cell'),
        ('TC', 'Training_Cell'),
        ('ST', 'Student'),
    )
    status = models.CharField(max_length=2, choices=choice,default='ST')
    def _str_(self):
        return self.user.username
    def __unicode__(self):
        return self.user.username
def post_save_user_model_reciever(sender,instance , created,*args,**kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass
post_save.connect(post_save_user_model_reciever,sender=settings.AUTH_USER_MODEL)