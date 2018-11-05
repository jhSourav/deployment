from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class StudentProfile(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.IntegerField()
    genderChoise = (('m', 'male'), ('f', 'female'))
    gender = models.CharField(max_length=50, choices=genderChoise)
    nationality = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    # def create_profile(sender, **kwargs):
    #     if kwargs['created']:
    #         user_profile = StudentProfile.objects.create(user=kwargs['instance'])
    #
    # post_save.connect(create_profile, sender=User)