# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from myproject.crm.models import Company


USER_DICT = {
    'username': 'jobconvo',
    'first_name': 'Job',
    'last_name': 'Convo',
    'email': 'job@convo.com',
    'password': 'demodemo',
}

try:
    user = User.objects.get(username='jobconvo')
except User.DoesNotExist:
    user = User.objects.create_user(**USER_DICT)
    user.is_superuser = True
    user.is_staff = True
    user.save()

COMPANY = ['Job Convo', 'Azz', 'Bit', 'Cadence', 'Dic', 'Xuan', 'Zion']

obj = [Company(name=name, user=user) for name in COMPANY]
Company.objects.bulk_create(obj)
