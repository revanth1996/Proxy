# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='pic',
            field=models.ImageField(upload_to=b''),
        ),
    ]
