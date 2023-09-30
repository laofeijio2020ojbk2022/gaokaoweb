"""django_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app01 import views


urlpatterns = [
    path('admin/add',views.admin_add),
    path('admin/<int:nid>/edit',views.user_edit),
    # 登录界面
    path('login/', views.login),
    path('register/', views.register),

    path('house/page', views.house_page),

    path('school/get', views.school_get),
    path('school/info', views.school_info),

    path('score/get', views.score_get),
    path('score/pre', views.score_pre),

    path('int/recom', views.int_recom),

    path('ana/sc', views.ana_sc),

]

