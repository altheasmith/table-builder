# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-18 02:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table_builder', '0002_tabledata'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TableData',
        ),
    ]
