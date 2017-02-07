# -*- coding: utf-8 -*-
import uuid
from django.db import models
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User
from myproject.core.models import TimeStampedModel


def _createHash():
    # Gera um uuid de 32 caracteres
    return str(uuid.uuid4())


class Company(TimeStampedModel):
    id = models.UUIDField(primary_key=True, unique=True,
                          editable=False, default=_createHash)
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
