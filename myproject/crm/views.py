# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView
from .mixins import CounterMixin
from .models import Company
from .forms import CompanyForm


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
            companies = Company.objects.all()
            data['html_company_list'] = render_to_string(
                'includes/partial_company_list.html', {'company_list': companies})
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


def company_update(request, uuid):
    company = get_object_or_404(Company, pk_uuid=uuid)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
    else:
        form = CompanyForm(instance=company)
    return company_create_form(request, form, 'crm/company_update.html')


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
    return JsonResponse(data)


class CompanyDetail(DetailView):
    model = Company
    slug_field = 'pk_uuid'
    slug_url_kwarg = 'uuid'
