# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .mixins import CounterMixin, SearchMixin, CompanyUpdateMixin, CompanyDeleteMixin
from .models import Company
from .forms import CompanyForm


class CompanyList(CounterMixin, SearchMixin, ListView):
    model = Company
    paginate_by = 10


class CompanyDetail(DetailView):
    model = Company
    slug_field = 'pk_uuid'
    slug_url_kwarg = 'uuid'


class CompanyUpdate(CompanyUpdateMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    slug_field = 'pk_uuid'
    slug_url_kwarg = 'uuid'


class CompanyDelete(CompanyDeleteMixin, DeleteView):
    model = Company
    slug_field = 'pk_uuid'
    slug_url_kwarg = 'uuid'


def company_create_form(request, form, template_name):
    data = {}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            companies = Company.objects.all()
            data['html_company_list'] = render_to_string(
                'includes/partial_company_list.html',
                {'company_list': companies},
                request=request)
            data['is_form_valid'] = True
        else:
            data['is_form_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(
        template_name, context, request=request)
    return JsonResponse(data)


def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
    else:
        form = CompanyForm()
    return company_create_form(request, form, 'crm/company_form.html')
