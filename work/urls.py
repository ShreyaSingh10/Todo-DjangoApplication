from django.conf.urls import url, include
from . import views
from django.contrib import admin

urlpatterns = [
   url(r'^$', views.index , name ='index')
]
""" When we use url(r'^$', views.index, name='index') it means the url should be
 address/posts/  ^$ means include nothing, so its gona look ito our views.py file
 for a method called index"""
