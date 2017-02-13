from django.conf.urls import include, url
from myproject.crm import views as c


re_uuid = r'^(?P<uuid>' + \
    r'\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/'

company_patterns = [
    url(r'^$', c.CompanyList.as_view(), name='company_list'),
    url(r'^add/$', c.company_create, name='company_add'),
    url(
        regex=re_uuid + r'$',
        view=c.CompanyDetail.as_view(),
        name='company_detail'
    ),
    url(
        regex=re_uuid + r'edit/$',
        view=c.CompanyUpdate.as_view(),
        name='company_update'
    ),
    url(
        regex=re_uuid + r'delete/$',
        view=c.CompanyDelete.as_view(),
        name='company_delete'
    ),
]

person_patterns = [
    url(r'^$', c.PersonList.as_view(), name='person_list'),
    url(r'^add/$', c.person_create, name='person_add'),
    url(
        regex=re_uuid + r'$',
        view=c.PersonDetail.as_view(),
        name='person_detail'
    ),
    url(
        regex=re_uuid + r'edit/$',
        view=c.PersonUpdate.as_view(),
        name='person_update'
    ),
    url(
        regex=re_uuid + r'delete/$',
        view=c.PersonDelete.as_view(),
        name='person_delete'
    ),
]

status_patterns = [
    url(r'^$', c.StatusList.as_view(), name='status_list'),
    url(r'^add/$', c.status_create, name='status_add'),
    url(
        regex=re_uuid + r'$',
        view=c.StatusDetailView.as_view(),
        name='status_detail'
    ),
    url(
        regex=re_uuid + r'edit/$',
        view=c.StatusUpdate.as_view(),
        name='status_update'
    ),
    url(
        regex=re_uuid + r'delete/$',
        view=c.StatusDelete.as_view(),
        name='status_delete'
    ),
]

product_patterns = [
    url(r'^$', c.ProductList.as_view(), name='product_list'),
    url(r'^add/$', c.product_create, name='product_add'),
]


urlpatterns = [
    url(r'^company/', include(company_patterns)),
    url(r'^person/', include(person_patterns)),
    url(r'^status/', include(status_patterns)),
    url(r'^product/', include(product_patterns)),
]
