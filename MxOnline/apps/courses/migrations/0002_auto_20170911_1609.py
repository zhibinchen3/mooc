# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 16:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='detial',
            new_name='detail',
        ),
    ]