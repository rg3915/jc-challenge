from django.contrib import admin
from .models import Company, Person, Status


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('pk_uuid', '__str__', 'user', 'created')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('pk_uuid', '__str__', 'company', 'user', 'created')


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'company', 'created')
