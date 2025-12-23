from django.urls import path
from .views import *
from .views import viewAbout

urlpatterns=[
    path('home/',viewHome, name='home'),
    path('about/',viewAbout, name='about'),
    path('service/',viewService, name='service'),
    path('department/',viewDepartment, name='department'),
    path('departmentsingle/',viewDepartmentSingle, name='departmentsingle'),
    path('doctors/',viewDoctors, name='doctor'),
    path('singledoctor/',viewSingleDoctors, name='singledoctor'),
    path('appoinment/',viewAppoinment, name='appoinment'),
    path('blocksidebar/',viewblock_sidebar, name='block_sidebar'),
    path('blocksingle/',viewblock_single, name='block_single'),
    path('contact/',viewcontact, name='contact'),

]