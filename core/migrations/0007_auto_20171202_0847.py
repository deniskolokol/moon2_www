# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-02 08:47
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20171201_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.URLField(max_length=500)),
                ('img_url', models.URLField(max_length=500)),
                ('order_id', models.IntegerField(default=0, help_text='Order in which logo appears in the stripe')),
            ],
        ),
        migrations.AlterField(
            model_name='content',
            name='column',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)]),
        ),
    ]
