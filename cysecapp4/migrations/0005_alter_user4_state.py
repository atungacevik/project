# Generated by Django 3.2.15 on 2022-08-10 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cysecapp4', '0004_user4_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user4',
            name='state',
            field=models.IntegerField(blank=True, default=False),
        ),
    ]
