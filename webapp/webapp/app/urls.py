from django.conf.urls import url
from . import views
from django.urls import path
from django.conf.urls import include
 
urlpatterns = [
    path('', views.index_template, name='index'),
    path('access.html/', views.access_template, name='access'),
    path('menu.html/', views.menu_template, name='menu'),
    path('works.html/', views.works_template, name='works'),
    path('staff.html/', views.staff_template, name='staff'),
    path('shop.html/', views.shop_template, name='shop'),
]