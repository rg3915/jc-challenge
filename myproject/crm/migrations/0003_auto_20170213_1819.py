# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20170213_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product',
            field=models.CharField(max_length=100, verbose_name=b'Produto'),
        ),
    ]
