
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', 'crasher.views.crasher'),
    url(r'detail/$', 'crasher.views.crasher_detail'),
]
