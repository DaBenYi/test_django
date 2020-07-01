from django.urls import path
from project_app import views

urlpatterns = [
    # 项目管理
    path('', views.project_manage),  # 首页面路径
    path('add_project/', views.add_project),#增加项目
    path('edit_project/<int:pid>/', views.edit_project),#编辑项目
    path('delete_project/<int:pid>/',views.delete_project),#删除项目

]
