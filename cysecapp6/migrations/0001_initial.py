# Generated by Django 3.2.15 on 2022-08-12 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, default=None, max_length=200, null=True, unique=True)),
                ('name', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('passwd', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('credit', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
    ]
