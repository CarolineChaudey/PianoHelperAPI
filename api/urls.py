from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.getAll, name='getAll'),
    url(r'^(?[0-9]+)$', views.get, name='get')
]
