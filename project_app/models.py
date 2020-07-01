from django.db import models

# Create your models here.
class Project(models.Model):
    '''
    自己创建的项目表
    '''
    name = models.CharField(max_length=50)
    describle = models.TextField(default="")
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=1)
    #返回项目名称
    def __str__(self):
        return  self.name