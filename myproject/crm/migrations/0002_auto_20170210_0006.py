# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='pk_uuid',
            field=models.UUIDField(null=True, default=uuid.uuid4, editable=False, unique=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='pk_uuid',
            field=models.UUIDField(null=True, default=uuid.uuid4, editable=False, unique=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='pk_uuid',
            field=models.UUIDField(null=True, default=uuid.uuid4, editable=False, unique=True, db_index=True),
        ),
    ]
