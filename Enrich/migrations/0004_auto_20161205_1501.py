# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 15:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Enrich', '0003_auto_20161205_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]