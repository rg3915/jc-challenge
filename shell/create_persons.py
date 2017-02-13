# -*- coding: utf-8 -*-
import names
import string
from random import choice
from django.contrib.auth.models import User
from myproject.crm.models import Company, Person

person_list = []
REPEAT = 9

USER_DICT = {
    'username': 'jobconvo',
    'first_name': 'Job',
    'last_name': 'Convo',
    'email': 'job@convo.com',
    'password': 'demodemo',
}


def gen_digits(max_length):
    return str(''.join(choice(string.digits) for i in range(max_length)))


def gen_phone():
    # gera um telefone no formato xx xxxxx-xxxx
    digits_ = gen_digits(11)
    return '{} 9{}-{}'.format(digits_[:2], digits_[3:7], digits_[7:])


def person_data():
    try:
        user = User.objects.get(username='jobconvo')
    except User.DoesNotExist:
        user = User.objects.create_user(**USER_DICT)
        user.is_superuser = True
        user.is_staff = True
        user.save()
    company = Company.objects.get(name='Job Convo')
    name = names.get_first_name() + ' ' + names.get_last_name()
    email = name.lower().strip() + '@email.com'
    phone = gen_phone()
    return {'name': name,
            'email': email,
            'phone': phone,
            'user': user,
            'company': company, }


# Appending person_list
for _ in range(REPEAT):
    person_list.append(person_data())

# Insert Persons
obj = [Person(**person) for person in person_list]
Person.objects.bulk_create(obj)
