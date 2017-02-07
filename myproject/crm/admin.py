from django.contrib import admin
from .models import Company, Person


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'user', 'created')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'company', 'user', 'created')
