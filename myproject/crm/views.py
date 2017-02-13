# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import resolve_url as r
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
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


class CompanyDetail(DetailView):
    model = Company
    slug_field = 'pk_uuid'
    slug_url_kwarg = 'uuid'


class CompanyUpdate(UpdateView):
    model = Company
    form_class = CompanyForm
    slug_field = 'pk_uuid'
    slug_url_kwarg = 'uuid'

    def get(self, request, *args, **kwargs):
        data = {}
        company = get_object_or_404(Company, pk_uuid=kwargs['uuid'])
        data['html_form'] = render_to_string(
            'crm/company_update.html',
            {'form': CompanyForm(instance=company)},
            request=request)
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        data = {}
        company = get_object_or_404(Company, pk_uuid=kwargs['uuid'])
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            company.save()
            company = Company.objects.get(pk_uuid=kwargs['uuid'])
            data['is_form_valid'] = True
            data['html_company_detail'] = render_to_string(
                'crm/company_detail_form.html',
                {'object': company},
                request=request)
        else:
            data['is_form_valid'] = False
            data['html_form'] = render_to_string(
                'crm/company_update.html', {'form': form}, request=request)

        return JsonResponse(data)


class CompanyDelete(DeleteView):
    model = Company
    slug_field = 'pk_uuid'
    slug_url_kwarg = 'uuid'

    def get(self, request, *args, **kwargs):
        data = {}
        company = get_object_or_404(Company, pk_uuid=kwargs['uuid'])
        context = {
            'form': CompanyForm(instance=company),
            'company': company,
        }
        data['html_form'] = render_to_string(
            'crm/company_delete.html', context=context, request=request)
        return HttpResponseRedirect(r('crm:company_list'))

    def post(self, request, *args, **kwargs):
        company = get_object_or_404(Company, pk_uuid=kwargs['uuid'])
        company.delete()
        return HttpResponseRedirect(r('crm:company_list'))


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
