# Generated by Django 3.2.15 on 2022-08-12 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cysecapp3', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user3',
            name='longitude',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
