# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 17:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0022_auto_20170510_1705'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['-topic']},
        ),
    ]
