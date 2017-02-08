from django.conf.urls import include, url
from myproject.crm import views as c

company_patterns = [
    url(r'^$', c.CompanyList.as_view(), name='company_list'),
    url(r'^add/$', c.company_create, name='company_add'),
    url(r'^(?P<pk>[\d\w\W-]+)/$', c.company_detail, name='company_detail'),
    url(r'^(?P<pk>[\d\w\W-]+)/edit/$', c.company_update, name='company_edit'),
    url(r'^(?P<pk>[\d\w\W-]+)/delete/$',
        c.company_delete, name='company_delete'),
]

urlpatterns = [
    url(r'^company/', include(company_patterns)),
]
