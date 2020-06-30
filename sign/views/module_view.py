from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models.module import Module
from sign.forms import ModuleForm

#模块管理页面
@login_required()
def module_manage(request):
    if request.method == "GET":
        module_all =Module.objects.all()
        return render(request, "module_manage.html",{'type':'list',
                                                     'modules':module_all})
@login_required()
def add_module(request):
    if request.method == "GET":
        module = ModuleForm()
        return render(request, "module_manage.html", {"type":"add","form":module})
    # elif request.method == "POST":
    #     project_name = request.POST.get("project_name", "")
    #     project_describle = request.POST.get("project_describle", "")
    #     status = request.POST.get("status", "")
    #     if project_name == "":
    #         return render(request, "project_manage.html", {"type":"add","name_error":"项目名称不能为空"})
    #     Project.objects.create(name=project_name,describle=project_describle,status=status)
    #     return HttpResponseRedirect('/project/')