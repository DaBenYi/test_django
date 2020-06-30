from django.db import models
from sign.models.project import Project
class Module(models.Model):
    '''
    自己创建的模块目表
    '''
    project = models.ForeignKey(Project,on_delete=models.CASCADE)#关联Project,models.CASCADE 项目删了，模块也删
    name = models.CharField("名称",max_length=50)#"名称" 后台会显示
    describle = models.TextField("描述",default="")
    create_time = models.DateTimeField(auto_now_add=True)
