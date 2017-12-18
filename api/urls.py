from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.get_all, name='getAll'),
    url(r'^(?P<music_id>[0-9]+)$', views.get, name='get')
]
