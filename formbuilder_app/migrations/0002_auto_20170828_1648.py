# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 15:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formbuilder_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Forms',
            new_name='Form',
        ),
    ]