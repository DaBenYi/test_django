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
from django.urls import path
from sign.views import login_view,project_view,module_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_view.index),
    path('index/', login_view.index),  # 登录路径
    path('logout/', login_view.logout),  # 退出登录
    path('accounts/login/', login_view.index),  # 重定向到登录路径

    # 模块管理
    path('module/', module_view.module_manage),#模块页面
    path('module/add_module/',module_view.add_module),#增加模块
    # 项目管理
    path('project/', project_view.project_manage),  # 首页面路径
    path('project/add_project/', project_view.add_project),#增加项目
    path('project/edit_project/<int:pid>/', project_view.edit_project),#编辑项目
    path('project/delete_project/<int:pid>/',project_view.delete_project),#删除项目



]
