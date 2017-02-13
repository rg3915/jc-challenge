# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import resolve_url as r
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from .models import Company, Person, Status
from .forms import CompanyForm, PersonForm, StatusForm


class CounterMixin(object):

    def get_context_data(self, **kwargs):
        context = super(CounterMixin, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context


class SearchCompanyMixin(object):

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


class SearchPersonMixin(object):

    def get_queryset(self):
        persons = Person.objects.all()
        q = self.request.GET.get('search_box')
        if q is not None:
            persons = persons.filter(name__icontains=q)
        return persons


class PersonUpdateMixin(object):

    def get(self, request, *args, **kwargs):
        data = {}
        person = get_object_or_404(Person, pk_uuid=kwargs['uuid'])
        data['html_form'] = render_to_string(
            'crm/person_update.html',
            {'form': PersonForm(instance=person)},
            request=request)
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        data = {}
        person = get_object_or_404(Person, pk_uuid=kwargs['uuid'])
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            person.save()
            person = Person.objects.get(pk_uuid=kwargs['uuid'])
            data['is_form_valid'] = True
            data['html_person_detail'] = render_to_string(
                'crm/person_detail_form.html',
                {'object': person},
                request=request)
        else:
            data['is_form_valid'] = False
            data['html_form'] = render_to_string(
                'crm/person_update.html', {'form': form}, request=request)
        return JsonResponse(data)


class PersonDeleteMixin(object):

    def get(self, request, *args, **kwargs):
        data = {}
        person = get_object_or_404(Person, pk_uuid=kwargs['uuid'])
        context = {
            'form': PersonForm(instance=person),
            'person': person,
        }
        data['html_form'] = render_to_string(
            'crm/person_delete.html', context=context, request=request)
        return HttpResponseRedirect(r('crm:person_list'))

    def post(self, request, *args, **kwargs):
        person = get_object_or_404(Person, pk_uuid=kwargs['uuid'])
        person.delete()
        return HttpResponseRedirect(r('crm:person_list'))


class SearchStatusMixin(object):

    def get_queryset(self):
        status = Status.objects.all()
        q = self.request.GET.get('search_box')
        if q is not None:
            status = status.filter(detail__icontains=q)
        return status


class StatusUpdateMixin(object):

    def get(self, request, *args, **kwargs):
        data = {}
        status = get_object_or_404(Status, pk_uuid=kwargs['uuid'])
        data['html_form'] = render_to_string(
            'crm/status_update.html',
            {'form': StatusForm(instance=status)},
            request=request)
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        data = {}
        status = get_object_or_404(Status, pk_uuid=kwargs['uuid'])
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            status.save()
            status = Status.objects.get(pk_uuid=kwargs['uuid'])
            data['is_form_valid'] = True
            data['html_status_detail'] = render_to_string(
                'crm/status_detail_form.html',
                {'object': status},
                request=request)
        else:
            data['is_form_valid'] = False
            data['html_form'] = render_to_string(
                'crm/status_update.html', {'form': form}, request=request)
        return JsonResponse(data)


class StatusDeleteMixin(object):

    def get(self, request, *args, **kwargs):
        data = {}
        status = get_object_or_404(Status, pk_uuid=kwargs['uuid'])
        context = {
            'form': StatusForm(instance=status),
            'status': status,
        }
        data['html_form'] = render_to_string(
            'crm/status_delete.html', context=context, request=request)
        return HttpResponseRedirect(r('crm:status_list'))

    def post(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk_uuid=kwargs['uuid'])
        status.delete()
        return HttpResponseRedirect(r('crm:status_list'))
