# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-25 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20171224_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='approvedBy',
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='leave',
            name='comment',
            field=models.TextField(blank=True, default=None),
        ),
    ]