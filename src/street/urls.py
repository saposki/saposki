
from django.conf.urls import url
from django.contrib import admin

from .views import(
    street,
    street_detail
)

urlpatterns = [
    url(r'^$', street),
    url(r'^detail/$', street_detail),
]
