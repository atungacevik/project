# Generated by Django 3.2.15 on 2022-08-15 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User9',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, default=None, max_length=900, null=True, unique=True)),
                ('name', models.CharField(blank=True, default=None, max_length=900, null=True)),
                ('passwd', models.CharField(blank=True, default=None, max_length=900, null=True)),
                ('course', models.CharField(blank=True, default=None, max_length=900, null=True)),
                ('auth_token', models.CharField(blank=True, default=None, max_length=900, null=True)),
                ('fail_count', models.IntegerField(default=0)),
            ],
        ),
    ]