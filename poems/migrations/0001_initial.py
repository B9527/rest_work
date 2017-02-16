# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=250)),
                ('type', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Poet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('dynasty', models.CharField(max_length=20, null=True, verbose_name=b'\xe6\x9c\x9d\xe4\xbb\xa3')),
                ('brief', models.CharField(max_length=250, null=True, verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b')),
                ('alias', models.CharField(max_length=20, null=True, verbose_name=b'\xe7\xa7\xb0\xe5\x8f\xb7')),
            ],
        ),
        migrations.AddField(
            model_name='poem',
            name='author',
            field=models.ForeignKey(to='poems.Poet', null=True),
        ),
    ]
