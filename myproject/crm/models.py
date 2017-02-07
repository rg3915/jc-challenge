# -*- coding: utf-8 -*-
from django.db import models
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User
from myproject.core.models import UUIDModel, TimeStampedModel


class Company(UUIDModel, TimeStampedModel):
    name = models.CharField('nome', max_length=50, unique=True)
    user = models.ForeignKey(
        User, verbose_name=u'usuário', related_name='company_user')

    class Meta:
        ordering = ['name']
        verbose_name = u'empresa'
        verbose_name_plural = u'empresas'

    def __unicode__(self):
        return self.name

    # def get_absolute_url(self):
    #     return r('crm:company_detail', pk=self.pk)


class Person(UUIDModel, TimeStampedModel):
    name = models.CharField('nome', max_length=50, unique=True)
    email = models.EmailField()
    phone = models.CharField('telefone', max_length=20, null=True, blank=True)
    user = models.ForeignKey(
        User, verbose_name=u'usuário', related_name='person_user')
    company = models.ForeignKey(
        'Company', verbose_name=u'empresa', related_name='person_company')

    class Meta:
        ordering = ['name']
        verbose_name = u'pessoa'
        verbose_name_plural = u'pessoas'

    def __unicode__(self):
        return self.name
