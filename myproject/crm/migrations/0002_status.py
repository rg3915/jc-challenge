# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import myproject.core.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=myproject.core.models._createHash, serialize=False, editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'modificado em')),
                ('detail', models.CharField(max_length=100, null=True, verbose_name=b'detalhe', blank=True)),
                ('next_contact', models.CharField(max_length=50, null=True, verbose_name='pr\xf3ximo contato', blank=True)),
                ('status', models.CharField(blank=True, max_length=2, null=True, verbose_name=b'tipo', choices=[(b'fu', b'fazer follow up'), (b'na', b'n\xc3\xa3o aprovado'), (b'su', b'sucesso')])),
                ('company', models.ForeignKey(related_name='status_company', verbose_name='empresa', to='crm.Company')),
                ('user', models.ForeignKey(related_name='status_user', verbose_name='usu\xe1rio', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
