# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test.utils import override_settings
from myproject.myauth.backends import EmailBackend


class EmailBackendTest(TestCase):

    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(
            username='regis',
            email='regis.santos.100@gmail.com',
            password='1234')
        self.backend = EmailBackend()

    def test_authenticate_with_email(self):
        user = self.backend.authenticate(
            email='regis.santos.100@gmail.com',
            password='1234')
        self.assertIsNotNone(user)

    def test_wrong_password(self):
        user = self.backend.authenticate(
            email='regis.santos.100@gmail.com',
            password='wrong')
        self.assertIsNone(user)

    def test_unknown_user(self):
        user = self.backend.authenticate(
            email='unknown@email.com',
            password='1324')
        self.assertIsNone(user)

    def test_get_user(self):
        self.assertIsNotNone(self.backend.get_user(1))


class MultipleEmailsTest(TestCase):

    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(
            username='user1',
            email='regis@email.com',
            password='1234')
        UserModel.objects.create_user(
            username='user2',
            email='regis@email.com',
            password='1234')
        self.backend = EmailBackend()

    def test_multiple_emails(self):
        user = self.backend.authenticate(
            email='regis@email.com', password='1234')
        self.assertIsNone(user)


@override_settings(AUTHENTICATION_BACKENDS=('myproject.myauth.backends.EmailBackend',))
class FunctionalEmailBackendTest(TestCase):

    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(
            username='regis',
            email='regis.santos.100@gmail.com',
            password='1234')

    def test_login_with_email(self):
        result = self.client.login(
            email='regis.santos.100@gmail.com',
            password='1234')
        self.assertTrue(result)

    def test_login_with_username(self):
        result = self.client.login(
            email='regis.santos.100@gmail.com',
            password='1234')
        self.assertTrue(result)
