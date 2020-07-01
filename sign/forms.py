from django import forms
from sign.models import Project
from sign.models import Module

class ProjectForm(forms.ModelForm):
    name = forms.CharField(label="名称",max_length=100)
    describle= forms.CharField(label="描述", max_length=100)
    status = forms.BooleanField(label="状态",required=True)

    class Meta:
        model = Project
        fields = ['name','describle','status']


class ModuleForm(forms.ModelForm):

    class Meta:
        model = Module
        fields = ['project','name', 'describle', ]