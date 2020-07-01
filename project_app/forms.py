from django import forms
from project_app.models import Project

class ProjectForm(forms.ModelForm):
    name = forms.CharField(label="名称",max_length=100)
    describle= forms.CharField(label="描述", max_length=100)
    status = forms.BooleanField(label="状态",required=True)

    class Meta:
        model = Project
        fields = ['name','describle','status']

