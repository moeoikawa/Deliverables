from django.conf.urls import url
from . import views
from django.urls import path
from django.conf.urls import include
 
urlpatterns = [
    path('', views.index_template, name='index'),
    path('access.html/', views.access_template, name='access'),
]