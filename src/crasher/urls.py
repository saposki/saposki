
from django.conf.urls import url
from django.contrib import admin

from .views import (
    crasher,
    crasher_detail
)

urlpatterns = [
    url(r'^$', crasher),
    url(r'detail/$', crasher_detail),
]
