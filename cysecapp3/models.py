from django.conf import settings
from django.db import models
from django.utils import timezone


class User3(models.Model):
    username = models.CharField(max_length=200, default=None, blank=True, null=True, unique=True)
    name = models.CharField(max_length=200, default=None, blank=True, null=True)
    latitude = models.CharField(max_length=200, default=None, blank=True, null=True)
    longitude = models.CharField(max_length=200, default=None, blank=True, null=True)
    deviceId = models.CharField(max_length=200, default=None, blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User3, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200, default=None, blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.user
