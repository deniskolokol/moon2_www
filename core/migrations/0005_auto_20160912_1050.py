# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-12 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160911_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='annotation',
            field=models.TextField(blank=True, null=True),
        ),
    ]
