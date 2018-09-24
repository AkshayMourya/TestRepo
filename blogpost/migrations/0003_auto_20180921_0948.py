# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0002_auto_20180921_0912'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='blog_post',
            table='blog_details_table',
        ),
    ]
