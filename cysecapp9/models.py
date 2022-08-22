from django.conf import settings
from django.db import models
from django.utils import timezone


class User9(models.Model):
    username = models.CharField(max_length=900, default=None, blank=True, null=True, unique=True)
    name = models.CharField(max_length=900, default=None, blank=True, null=True)
    passwd = models.CharField(max_length=900, default=None, blank=True, null=True)
    course = models.CharField(max_length=900, default=None, blank=True, null=True)
    auth_token = models.CharField(max_length=900, default=None, blank=True, null=True)
    fail_count = models.IntegerField(default=0, null=False)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
