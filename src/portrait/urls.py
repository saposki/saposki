
from django.conf.urls import url
from django.contrib import admin

from .views import(
    portrait,
    portrait_detail
)

urlpatterns = [
    url(r'^$', portrait),
    url(r'^detail/$', portrait_detail),
]
