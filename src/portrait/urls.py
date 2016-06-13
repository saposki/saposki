
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', 'portrait.views.portrait'),
    url(r'^portrait/$', 'portrait.views.portrait'),
]
