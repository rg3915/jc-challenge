from django.conf.urls import include, url
from myproject.crm import views as c


re_detail = r'^(?P<uuid>' + \
    r'\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/'
re_update = re_detail + r'edit/'

company_patterns = [
    url(r'^$', c.CompanyList.as_view(), name='company_list'),
    url(r'^add/$', c.company_create, name='company_add'),
    url(
        regex=re_detail + r'$',
        view=c.CompanyDetail.as_view(),
        name='company_detail'
    ),
    url(
        regex=re_update + r'$',
        view=c.CompanyUpdate.as_view(),
        name='company_edit'
    ),
    url(r'^(?P<pk>[\d\w\W-]+)/delete/$',
        c.company_delete, name='company_delete'),
]

urlpatterns = [
    url(r'^company/', include(company_patterns)),
]
