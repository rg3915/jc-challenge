# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import resolve_url as r
from django.utils.formats import number_format
from myproject.core.models import UUIDModel, TimeStampedModel
from .lists import STATUS


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

    def get_absolute_url(self):
        return r('crm:company_detail', uuid=self.pk_uuid)


class Person(UUIDModel, TimeStampedModel):
    name = models.CharField('nome', max_length=50, unique=True)
    email = models.EmailField()
    phone = models.CharField('telefone', max_length=20, null=True, blank=True)
    user = models.ForeignKey(
        User, verbose_name=u'usuário', related_name='person_user')
    company = models.ForeignKey(
        'Company', verbose_name='empresa', related_name='person_company')

    class Meta:
        ordering = ['name']
        verbose_name = u'pessoa'
        verbose_name_plural = u'pessoas'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return r('crm:person_detail', uuid=self.pk_uuid)


class Status(UUIDModel, TimeStampedModel):
    user = models.ForeignKey(
        User, verbose_name=u'usuário', related_name='status_user')
    company = models.ForeignKey(
        'Company', verbose_name='empresa', related_name='status_company')
    detail = models.CharField('detalhe', max_length=100, null=True, blank=True)
    next_contact = models.CharField(
        u'próximo contato', max_length=50, null=True, blank=True)
    status = models.CharField('tipo', max_length=2,
                              choices=STATUS, null=True, blank=True)

    class Meta:
        ordering = ['-created']
        verbose_name = u'status'
        verbose_name_plural = u'status'

    def __unicode__(self):
        return self.detail

    def get_absolute_url(self):
        return r('crm:status_detail', uuid=self.pk_uuid)


class Product(models.Model):
    product = models.CharField('Produto', max_length=100, unique=True)
    price = models.DecimalField('Preço', max_digits=7, decimal_places=2)

    class Meta:
        ordering = ['product']
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

    def __unicode__(self):
        return self.product

    def get_price(self):
        return "R$ %s" % number_format(self.price, 2)


class StatusDetail(models.Model):
    status = models.ForeignKey('Status', related_name='status_det')
    product = models.ForeignKey(
        Product, related_name='product_det', verbose_name='produto')
    quantity = models.PositiveSmallIntegerField('quantidade')
    price = models.DecimalField(
        u'Preço', max_digits=6, decimal_places=2, default=0)

    def __unicode__(self):
        return str(self.status)

    def get_subtotal(self):
        return self.price * (self.quantity or 0)

    subtotal = property(get_subtotal)

    def price_formated(self):
        return "R$ %s" % number_format(self.price, 2)

    def subtotal_formated(self):
        return "R$ %s" % number_format(self.subtotal, 2)
