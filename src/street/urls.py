
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', 'street.views.street'),
    url(r'^street/$', 'street.views.street'),
]
