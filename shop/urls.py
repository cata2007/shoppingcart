from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('list/', views.product_list, name='person')
]
