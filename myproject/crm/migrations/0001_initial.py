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
                'ordering': ['-created'],
                'verbose_name': 'status',
                'verbose_name_plural': 'status',
            },
        ),
        migrations.CreateModel(
            name='StatusDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveSmallIntegerField(verbose_name=b'quantidade')),
                ('price', models.DecimalField(default=0, verbose_name='Pre\xe7o', max_digits=6, decimal_places=2)),
                ('product', models.ForeignKey(related_name='product_det', verbose_name=b'produto', to='crm.Product')),
                ('status', models.ForeignKey(related_name='status_det', to='crm.Status')),
            ],
        ),
    ]
