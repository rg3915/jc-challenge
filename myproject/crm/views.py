# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .mixins import *
from .models import Company, Person
from .forms import CompanyForm, PersonForm


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


class CompanyList(CounterMixin, SearchCompanyMixin, ListView):
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


def person_create_form(request, form, template_name):
    data = {}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            persons = Person.objects.all()
            data['html_person_list'] = render_to_string(
                'includes/partial_person_list.html',
                {'person_list': persons},
                request=request)
            data['is_form_valid'] = True
        else:
            data['is_form_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(
        template_name, context, request=request)
    return JsonResponse(data)


def person_create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
    else:
        form = PersonForm()
    return person_create_form(request, form, 'crm/person_form.html')


class PersonList(CounterMixin, SearchPersonMixin, ListView):
    model = Person
    paginate_by = 15


class PersonDetail(DetailView):
    model = Person
    slug_field = 'pk_uuid'
    slug_url_kwarg = 'uuid'


class PersonUpdate(PersonUpdateMixin, UpdateView):
    model = Person
    form_class = PersonForm
    slug_field = 'pk_uuid'
    slug_url_kwarg = 'uuid'


class PersonDelete(PersonDeleteMixin, DeleteView):
    model = Person
    slug_field = 'pk_uuid'
    slug_url_kwarg = 'uuid'
