from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'', include('myproject.core.urls', namespace='core')),
    url(r'^crm/', include('myproject.crm.urls', namespace='crm')),
    url(r'^admin/', admin.site.urls),
]
