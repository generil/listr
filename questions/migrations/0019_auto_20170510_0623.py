# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 06:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0018_auto_20170510_0621'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-question_date']},
        ),
    ]
