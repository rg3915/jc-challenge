from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from django.test import TestCase
from myproject.crm.models import Company, Person
from myproject.crm.tests import USER_DICT, COMPANY_DICT, PERSON_DICT


class PersonTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(**USER_DICT)
        self.company = Company.objects.create(user=self.user, **COMPANY_DICT)
        self.obj = Person.objects.create(
            user=self.user, company=self.company, **PERSON_DICT)

    def test_create(self):
        self.assertTrue(Person.objects.exists())

    def test_len_uuid(self):
        self.assertEqual(len(self.obj.id), 36)

    def test_uuid_is_str(self):
        self.assertIs(type(self.obj.id), str)

    def test_created(self):
        ''' Person must have an auto created attr. '''
        self.assertIsInstance(self.obj.created, datetime)

    def test_str(self):
        self.assertEqual('Regis', str(self.obj))

    def test_ordering(self):
        self.assertListEqual(['name'], Person._meta.ordering)

    # def test_get_absolute_url(self):
    #     url = r('crm:person_detail', pk=self.obj.pk)
    #     self.assertEqual(url, self.obj.get_absolute_url())
