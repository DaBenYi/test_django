from django.contrib import admin
from module_app.models import Module

# Register your models here.
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name','describle','create_time','project']
    search_fields = ['name']#根据名字搜素
    list_filter = ['create_time']#根据创建时间过滤
admin.site.register(Module,ModuleAdmin)