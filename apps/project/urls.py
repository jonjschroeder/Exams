from django.conf.urls import url
from . import views

urlpatterns = [

    # displays users trips and other's trips
    url(r'^$', views.appoints, name='appoints'),
    url(r'^process$', views.process, name='process'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name = 'delete'),
]
