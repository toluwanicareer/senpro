# Generated by Django 3.1.3 on 2020-12-28 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='upfile',
            field=models.BooleanField(default=False),
        ),
    ]