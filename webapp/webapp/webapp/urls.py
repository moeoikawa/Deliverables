from django.contrib import admin
from django.urls import path
from django.conf.urls import include

"""
adminページを表示させるためには以下を実行
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
参考URL：https://djangobrothers.com/tutorials/blog_app/model/
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    
]
