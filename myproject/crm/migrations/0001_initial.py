# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pk_uuid', models.UUIDField(default=uuid.uuid4, unique=True, editable=False, db_index=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pk_uuid', models.UUIDField(default=uuid.uuid4, unique=True, editable=False, db_index=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'modificado em')),
                ('name', models.CharField(unique=True, max_length=50, verbose_name=b'nome')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20, null=True, verbose_name=b'telefone', blank=True)),
                ('company', models.ForeignKey(related_name='person_company', verbose_name=b'empresa', to='crm.Company')),
                ('user', models.ForeignKey(related_name='person_user', verbose_name='usu\xe1rio', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'pessoa',
                'verbose_name_plural': 'pessoas',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pk_uuid', models.UUIDField(default=uuid.uuid4, unique=True, editable=False, db_index=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'modificado em')),
                ('detail', models.CharField(max_length=100, null=True, verbose_name=b'detalhe', blank=True)),
                ('next_contact', models.CharField(max_length=50, null=True, verbose_name='pr\xf3ximo contato', blank=True)),
                ('status', models.CharField(blank=True, max_length=2, null=True, verbose_name=b'tipo', choices=[(b'fu', b'fazer follow up'), (b'na', b'n\xc3\xa3o aprovado'), (b'su', b'sucesso')])),
                ('company', models.ForeignKey(related_name='status_company', verbose_name=b'empresa', to='crm.Company')),
                ('user', models.ForeignKey(related_name='status_user', verbose_name='usu\xe1rio', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
