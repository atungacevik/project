# Generated by Django 3.2.15 on 2022-08-10 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cysecapp4', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user4',
            name='auth_token',
        ),
        migrations.RemoveField(
            model_name='user4',
            name='course',
        ),
        migrations.AddField(
            model_name='user4',
            name='otp',
            field=models.IntegerField(blank=True, default=None, max_length=200, null=True),
        ),
    ]