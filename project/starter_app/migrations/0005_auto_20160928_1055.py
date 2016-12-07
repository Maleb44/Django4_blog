# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starter_app', '0004_auto_20160922_1620'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='message',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
