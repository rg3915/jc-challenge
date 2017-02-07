# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import myproject.core.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=myproject.core.models._createHash, serialize=False, editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'modificado em')),
                ('name', models.CharField(unique=True, max_length=50, verbose_name=b'nome')),
                ('user', models.ForeignKey(related_name='company_user', verbose_name='usu\xe1rio', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'empresa',
                'verbose_name_plural': 'empresas',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=myproject.core.models._createHash, serialize=False, editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'modificado em')),
                ('name', models.CharField(unique=True, max_length=50, verbose_name=b'nome')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20, null=True, verbose_name=b'telefone', blank=True)),
                ('company', models.ForeignKey(related_name='person_company', verbose_name='empresa', to='crm.Company')),
                ('user', models.ForeignKey(related_name='person_user', verbose_name='usu\xe1rio', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'pessoa',
                'verbose_name_plural': 'pessoas',
            },
        ),
    ]
