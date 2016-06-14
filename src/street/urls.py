
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', 'street.views.street'),
    url(r'^detail/$', 'street.views.street_detail'),
]
