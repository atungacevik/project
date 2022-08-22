from django.conf import settings
from django.db import models
from django.utils import timezone


class User4(models.Model):
    username = models.CharField(max_length=200, default=None, blank=True, null=True, unique=True)
    name = models.CharField(max_length=200, default=None, blank=True, null=True)
    passwd = models.CharField(max_length=200, default=None, blank=True, null=True)
    auth_token = models.CharField(max_length=200, default=None, blank=True, null=True)
    otp = models.IntegerField(max_length=200, default=None, blank=True, null=True)
    state = models.IntegerField(default=False, blank=True, null=False)
    try_count = models.IntegerField(default=False, blank=True, null=False)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
