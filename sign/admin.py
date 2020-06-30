from django.contrib import admin
from sign.models.project import Project
from sign.models.module import Module
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name','describle','create_time']
    #还有其他功能，比如搜素框、过滤器
    search_fields = ['name']#根据名字搜素
    list_filter = ['create_time']#根据创建时间过滤
admin.site.register(Project,ProjectAdmin)

class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name','describle','create_time','project']
    search_fields = ['name']#根据名字搜素
    list_filter = ['create_time']#根据创建时间过滤
admin.site.register(Module,ModuleAdmin)