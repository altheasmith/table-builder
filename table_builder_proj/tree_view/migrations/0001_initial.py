# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-18 04:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TreeNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('icon', models.CharField(blank=True, max_length=50, null=True)),
                ('selectedIcon', models.CharField(blank=True, max_length=50, null=True)),
                ('color', models.CharField(blank=True, max_length=15, null=True)),
                ('backColor', models.CharField(blank=True, max_length=15, null=True)),
                ('href', models.CharField(blank=True, max_length=15, null=True)),
                ('selectable', models.NullBooleanField()),
                ('parentNode', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tree_view.TreeNode')),
            ],
        ),
    ]
