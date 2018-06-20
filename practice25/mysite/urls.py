from django.conf.urls import patterns,include,url
from django.contrib import admin

urlpatterns = patterns('',
        url(r'^admin/',include(admin.site.urls)),
        url(r'^todolist/',include('todolist.urls')),
        url(r'^',include('todolist.urls')),
        )
