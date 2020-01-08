from django.db import models

class Memo(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


"""
新しくアプリケーションを追加する場合は、setting.pyに追記する

C:/User/moeoi/Desktop/webapp/webapp/setting.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',      ←ここに追記
]

"""