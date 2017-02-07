from django.conf.urls import url
from myproject.core.views import home


urlpatterns = [
    url(r'^$', home, name='home'),
]
