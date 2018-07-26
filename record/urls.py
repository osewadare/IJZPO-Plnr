from django.conf.urls import url
from .import views
from django_filters.views import FilterView
from .filters import applicationsfilter


app_name = 'records'

urlpatterns = [
    url(r'^$', views.indexview.as_view(), name='index'),
    url(r'^applications$', views.applicationsview.as_view(), name='applications'),
    url(r'^map$', views.mapsview.as_view(), name='maps'),
    url(r'^new$', views.CreateApplication.as_view(), name='createapplication'),
    url(r'^update/(?P<pk>[0-9]+)$', views.applicationupdate.as_view(), name='updateapplication'),
    url(r'^delete/(?P<pk>[0-9]+)$', views.applicationdelete.as_view(), name='deleteapplication'),
    url(r'^search/$', views.search, name='search'),
    url(r'^staffprofile/$', views.staffview.as_view(), name='staff_profile'),
    url(r'^addstaff/$', views.AddStaff.as_view(), name='addstaff')

 ]