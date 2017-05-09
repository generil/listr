# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 14:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_auto_20170506_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=15, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30, unique=True)),
                ('institution', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=30)),
                ('join_date', models.DateField(auto_now_add=True)),
                ('is_verified', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='answer',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='question',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='create_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='answer',
            name='respondent',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='questions.Person'),
        ),
        migrations.AddField(
            model_name='comment',
            name='commenter',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='questions.Person'),
        ),
        migrations.AddField(
            model_name='question',
            name='questioner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='questions.Person'),
        ),
        migrations.AddField(
            model_name='topic',
            name='creator',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='questions.Person'),
        ),
    ]