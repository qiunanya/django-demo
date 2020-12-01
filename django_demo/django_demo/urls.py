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
from django.shortcuts import HttpResponse, render, redirect
from requestApi import class_actioin

admin.site.site_url="http://localhost:8081/index"

def login(request):
    """
    处理用户请求，并返回内容
    :HttpResponse 返回对象或者字符串
    :param request: 用户请求相关的所有信息（对象）
    :return:
    """
    print(request.method)
    if request.method == 'GET':
       return render(request, 'user/login.html')
    else:
        print(request.POST)
        # 不能直接用getkeys，用get，没有会默认为null，否则报错
        name = request.POST.get('username')
        pwd = request.POST.get("password")
        if name == 'admin' and pwd == '123456':
            # return redirect('http://39.106.29.92')
            # 自定义首页
            return redirect('/index/')
        else:
            # 登录失败
            msg = {'msg': '用户名或密码错误'}
            # return HttpResponse(msg)
            return render(request, 'user/login.html', msg)
            pass
        pass
    pass

def welcome(request):
    """
    处理用户请求，并返回内容
    :param request: 用户请求相关的所有信息（对象）
    :return:
    """
    return HttpResponse("欢迎使用Django 框架")
    pass
def index(request):
    return render(request, 'home.html', {
        "master": "邱南亚的博客",
        "list":['礼节', '方云'],
        "dict": {'k': 'ddddd', 'v': 'dssdssfds'}
    })
    pass
urlpatterns = [
    path('welcome/', welcome),
    path('login/', login),
    path('index/', index),
    path('class/', class_actioin.classes),
    path('add_class/', class_actioin.add_class),
    path('del_class/', class_actioin.del_class),
    path('edit_class/', class_actioin.edit_class)
]
