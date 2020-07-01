"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from user_app import views
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),

    #用户应用
    path('',views.index),
    path('index/', views.index),  # 登录路径
    path('logout/', views.logout),  # 退出登录
    path('accounts/login/', views.index),  # 重定向到登录路径

    # 项目管理
    path('project/', include('project_app.urls')),
    # 模块管理
    path('module/', include('module_app.urls')),

]
