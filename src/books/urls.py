from django.conf import settings
from django.conf.urls.contrib import  admin
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(""))
]