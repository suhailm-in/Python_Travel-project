
from . import views
from django.urls import path

urlpatterns = [

    # path('',views.demo,name='demo'),
    path('',views.index,name='index'),
    # path('abouta/',views.abouta,name='abouta'),
    path('contact/',views.contact,name='contact'),
    path('add/',views.addition,name='addition'),
]
