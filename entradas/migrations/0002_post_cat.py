# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0004_auto_20160925_1402'),
        ('entradas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cat',
            field=models.ManyToManyField(to='categorias.categorias'),
        ),
    ]
