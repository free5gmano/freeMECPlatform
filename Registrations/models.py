from django.db import models
from django.contrib.auth.models import User as us
from django.contrib.auth.models import AbstractUser


class MecApp(AbstractUser):
    role = models.CharField(max_length=20, default='unverified')

class AppInfo(models.Model):
    appName = models.CharField(max_length=64, default='unverified')
    appProvider = models.CharField(max_length=64, default='unverified')
    appCategory = models.CharField(max_length=64, default='unverified')
    appDId = models.CharField(max_length=64, default='unverified')
    appInstanceId = models.CharField(max_length=64, default='unverified')
    endpoint = models.CharField(max_length=64, default='unverified')
    appServiceRequired = models.CharField(max_length=64, default='unverified')
    appServiceOptional = models.CharField(max_length=64, default='unverified')
    appFeatureRequired = models.CharField(max_length=64, default='unverified')
    appFeatureOptional = models.CharField(max_length=64, default='unverified')
    isInsByMec = models.CharField(max_length=64, default='unverified')
    appProfile = models.CharField(max_length=64, default='unverified')
