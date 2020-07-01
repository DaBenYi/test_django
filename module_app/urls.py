from module_app import views
from django.urls import path,include


urlpatterns = [
    # 模块管理
    path('', views.module_manage),#模块页面
    path('add_module/',views.add_module),#增加模块
    path('edit_module/<int:mid>/', views.edit_module),  # 编辑模块
    path('delete_module/<int:mid>/', views.delete_module),  # 删除项目
]