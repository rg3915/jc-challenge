from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from django.test import TestCase
from myproject.crm.models import Company
from myproject.crm.tests import USER_DICT, COMPANY_DICT


class CustomerTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(**USER_DICT)
        self.obj = Company.objects.create(user=self.user, **COMPANY_DICT)

    def test_create(self):
        self.assertTrue(Company.objects.exists())

    def test_len_uuid(self):
        self.assertEqual(len(self.obj.pk_uuid), 32)

    def test_uuid_is_str(self):
        self.assertIs(type(self.obj.pk_uuid), str)

    def test_created(self):
        ''' Company must have an auto created attr. '''
        self.assertIsInstance(self.obj.created, datetime)

    def test_str(self):
        self.assertEqual('Job Convo', str(self.obj))

    def test_ordering(self):
        self.assertListEqual(['name'], Company._meta.ordering)

    # def test_get_absolute_url(self):
    #     url = r('crm:company_detail', pk=self.obj.pk)
    #     self.assertEqual(url, self.obj.get_absolute_url())
