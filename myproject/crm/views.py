# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy as r
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Company
from .forms import CompanyForm


class CompanyList(ListView):
    model = Company
    paginate_by = 10


class CompanyCreate(CreateView):
    template_name = 'crm/company_form.html'
    form_class = CompanyForm
    success_url = r('crm:company_list')
