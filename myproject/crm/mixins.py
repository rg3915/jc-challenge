# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import resolve_url as r
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from .models import Company
from .forms import CompanyForm


class CounterMixin(object):

    def get_context_data(self, **kwargs):
        context = super(CounterMixin, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context


class SearchMixin(object):

    def get_queryset(self):
        companies = Company.objects.all()
        q = self.request.GET.get('search_box')
        if q is not None:
            companies = companies.filter(name__icontains=q)
        return companies


class CompanyUpdateMixin(object):

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


class CompanyDeleteMixin(object):

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
