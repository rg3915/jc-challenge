# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product', models.CharField(unique=True, max_length=100, verbose_name=b'Produto')),
                ('price', models.DecimalField(verbose_name=b'Pre\xc3\xa7o', max_digits=7, decimal_places=2)),
            ],
            options={
                'ordering': ['product'],
                'verbose_name': 'produto',
                'verbose_name_plural': 'produtos',
            },
        ),
        migrations.CreateModel(
            name='StatusDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveSmallIntegerField(verbose_name=b'quantidade')),
                ('price', models.DecimalField(default=0, verbose_name='Pre\xe7o', max_digits=6, decimal_places=2)),
                ('product', models.ForeignKey(related_name='product_det', verbose_name=b'produto', to='crm.Product')),
            ],
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'ordering': ['-created'], 'verbose_name': 'status', 'verbose_name_plural': 'status'},
        ),
        migrations.AddField(
            model_name='statusdetail',
            name='status',
            field=models.ForeignKey(related_name='status_det', to='crm.Status'),
        ),
    ]
