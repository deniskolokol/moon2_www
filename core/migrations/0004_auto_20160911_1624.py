# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-11 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_unit_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='token',
            field=models.CharField(db_index=True, max_length=20),
        ),
    ]