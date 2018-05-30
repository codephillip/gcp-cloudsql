from django.conf.urls import url

from myapp.views import home

urlpatterns = [
    url(r'', home, name='home')
]
