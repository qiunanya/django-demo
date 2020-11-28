"""django_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse

admin.site.site_url="http://localhost:8081/index"

def login(request):
    """
    处理用户请求，并返回内容
    :param request: 用户请求相关的所有信息（对象）
    :return:
    """
    return HttpResponse("login")
    pass

def welcome(request):
    """
    处理用户请求，并返回内容
    :param request: 用户请求相关的所有信息（对象）
    :return:
    """
    return HttpResponse("欢迎使用Django 框架")
    pass

urlpatterns = [
    path('welcome/', welcome),
    path('login/', login)
]
