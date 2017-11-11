from django.conf.urls import url
from django.contrib import admin
from .views import problems

urlpatterns = [
    url(r'^', problems, name="problems"),
    url(r'^problems/$', problems, name="problems"),
]
