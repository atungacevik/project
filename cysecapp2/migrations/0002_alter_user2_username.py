# Generated by Django 3.2.15 on 2022-08-10 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cysecapp2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user2',
            name='username',
            field=models.CharField(blank=True, default=None, max_length=200, null=True, unique=True),
        ),
    ]
