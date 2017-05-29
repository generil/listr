# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-29 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0035_auto_20170518_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='description',
            field=models.CharField(default=b'description', max_length=50),
        ),
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.FileField(blank=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='person',
            name='institution',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='position',
            field=models.CharField(max_length=50),
        ),
    ]