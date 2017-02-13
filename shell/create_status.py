# -*- coding: utf-8 -*-
from random import randint, choice
from django.contrib.auth.models import User
from myproject.crm.models import Company, Status

status_list = []
REPEAT = 9

USER_DICT = {
    'username': 'jobconvo',
    'first_name': 'Job',
    'last_name': 'Convo',
    'email': 'job@convo.com',
    'password': 'demodemo',
}


def status_data():
    try:
        user = User.objects.get(username='jobconvo')
    except User.DoesNotExist:
        user = User.objects.create_user(**USER_DICT)
        user.is_superuser = True
        user.is_staff = True
        user.save()
    company = Company.objects.get(name='Job Convo')
    detail = choice(['Lorem', 'ipsum', 'dolor', 'sit',
                     'amet', 'consectetur', 'adipisicing', 'elit'])
    next_contact = str(randint(1, 12)) + '/' + str(randint(1, 12)) + '/2017'
    status = choice(['fu', 'na', 'su'])
    return {'user': user,
            'company': company,
            'detail': detail,
            'next_contact': next_contact,
            'status': status, }


# Appending status_list
for _ in range(REPEAT):
    status_list.append(status_data())

# Insert Status
obj = [Status(**status) for status in status_list]
Status.objects.bulk_create(obj)
