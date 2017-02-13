# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import resolve_url as r
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView
from .mixins import CounterMixin
from .models import Company, Person
from .forms import CompanyForm, PersonForm


class CompanyList(CounterMixin, ListView):
    model = Company
    paginate_by = 10

    def get_queryset(self):
        companies = Company.objects.all()
        q = self.request.GET.get('search_box')
        if q is not None:
            companies = companies.filter(name__icontains=q)
        return companies


def company_create_form(request, form, template_name):
    data = {}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # companies = Company.objects.all()
            # data['html_company_list'] = render_to_string(
            # 'includes/partial_company_list.html', {'company_list': companies})
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


def company_update_form(request, form, template_name, uuid):
    data = {}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            company = Company.objects.get(pk_uuid=uuid)
            data['html_company_list'] = render_to_string(
                'company_detail.html', {'object': company})
            data['is_form_valid'] = True
        else:
            data['is_form_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(
        template_name, context, request=request)

    return JsonResponse(data)


def company_update(request, uuid):
    company = get_object_or_404(Company, pk_uuid=uuid)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
    else:
        form = CompanyForm(instance=company)
    return company_update_form(request, form, 'crm/company_update.html', uuid)


def company_delete(request, uuid):
    data = {}
    company = get_object_or_404(Company, pk_uuid=uuid)
    if request.method == 'POST':
        data['is_form_valid'] = True
        company.delete()
        companies = Company.objects.all()
        data['html_company_list'] = render_to_string(
            'includes/partial_company_list.html', {'company_list': companies})
    else:
        form = CompanyForm(instance=company)
        context = {
            'empresa': company,
            'form': form}
        data['html_form'] = render_to_string(
            'crm/company_delete.html', context, request=request)
    return HttpResponseRedirect(r('crm:company_list'))


class CompanyDetail(DetailView):
    model = Company
    slug_field = 'pk_uuid'
    slug_url_kwarg = 'uuid'


class PersonList(CounterMixin, ListView):
    model = Person
    paginate_by = 10

    def get_queryset(self):
        persons = Person.objects.all()
        q = self.request.GET.get('search_box')
        if q is not None:
            persons = persons.filter(name__icontains=q)
        return persons


def person_create_form(request, form, template_name):
    data = {}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            persons = Person.objects.all()
            data['html_person_list'] = render_to_string(
                'includes/partial_person_list.html', {'person_list': persons})
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
