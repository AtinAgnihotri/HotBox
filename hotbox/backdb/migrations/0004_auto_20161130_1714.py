# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 17:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backdb', '0003_subs_forum_subs_subforum_subs_thread_subs_users'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tag_to_thread',
            new_name='tag_to_forum',
        ),
        migrations.RemoveField(
            model_name='user',
            name='subs_user',
        ),
        migrations.AlterField(
            model_name='tag_to_forum',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backdb.Forums'),
        ),
    ]