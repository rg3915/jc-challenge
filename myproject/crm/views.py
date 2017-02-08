# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import ListView
from .mixins import CounterMixin
from .models import Company
from .forms import CompanyForm


class CompanyList(CounterMixin, ListView):
    model = Company
    paginate_by = 10

    def get_queryset(self):
        w = Company.objects.all()
        q = self.request.GET.get('search_box')
        if q is not None:
            w = w.filter(name__icontains=q)
        return w


def company_create_form(request, form, template_name):
    data = {}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
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
