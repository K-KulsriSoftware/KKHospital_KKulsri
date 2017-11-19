"""kkhospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import allauth

import app.views

urlpatterns = [
    url(r'^$', app.views.home, name='home'),
    url(r'^departments/', app.views.departments, name='departments'),
    url(r'^about', app.views.about, name='about'),
    url(r'^doctor-detail/', app.views.doctor_detail, name='doctor_detail'),
    url(r'^regular-packages/', app.views.regular_packages, name='regular_packages'),
    url(r'^special-packages/(?P<package_id>\w{0,50})/$',
        app.views.special_packages, name='special_packages'),
    url(r'^doctor-search/', app.views.search_for_doctor, name='search_for_doctor'),
    url(r'^doctor/$', app.views.doctor, name='doctor'),
    url(r'^confirm/', app.views.confirm, name='confirm'),
    url(r'^payment/', app.views.payment, name='payment'),
    url(r'^admin-mongo/$', app.views.admin_mongo, name='admin_mongo'),
    url(r'^admin-mongo/collection/(?P<collection_name>\w{0,50})/$',
        app.views.admin_mongo_collection, name='admin_mongo-collection'),
    url(r'^admin-mongo/collection/(?P<collection_name>\w{0,50})/add/$',
        app.views.admin_mongo_add, name='admin_mongo-add'),
    url(r'^admin-mongo/collection/(?P<collection_name>\w{0,50})/edit/(?P<object_id>\w{0,50})$',
        app.views.admin_mongo_edit, name='admin_mongo-edit'),
    url(r'^admin-mongo/collection/(?P<collection_name>\w{0,50})/delete/(?P<object_id>\w{0,50})$',
        app.views.admin_mongo_delete, name='admin_mongo-delete'),
    url(r'^doctor_search_api/', app.views.doctor_search_api,
        name='doctor_search_api'),
    url(r'^doctor_auto_search_api/', app.views.doctor_auto_search_api,
        name='doctor_auto_search_api'),
    url(r'^check-user-information/', app.views.check_user_information,name='check_user_information'),

    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^member/$', app.views.member, name='member'),
    url(r'^member/edit/$', app.views.edit_member_info, name='edit_member_info'),
    url(r'^register/$', app.views.register, name='register'),
    url(r'^doctor-profile/$', app.views.doctor_profile, name='doctor-profile'),
    url(r'^member/profile/$', app.views.member, name='member-profile'),
]
