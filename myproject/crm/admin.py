from django.contrib import admin
from .models import Company, Person, Status, StatusDetail, Product


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('pk_uuid', '__str__', 'user', 'created')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('pk_uuid', '__str__', 'company', 'user', 'created')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ['product']
    list_display = ('product', 'get_price')
    search_fields = ('product',)


class StatusDetailInline(admin.TabularInline):
    list_display = ['product', 'quantity', 'price']
    readonly_fields = ['get_subtotal']
    model = StatusDetail
    extra = 0


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'company', 'created')
    # readonly_fields = ['get_total']
    date_hierarchy = 'created'
    inlines = [StatusDetailInline]
