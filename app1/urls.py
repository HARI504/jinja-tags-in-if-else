from django.urls import path
from django.urls import path
from app1.views import *
app_name='app1'
urlpatterns=[
    path('head1/',head1,name='head1'),
]