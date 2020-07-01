from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from module_app.models import Module
from module_app.forms import ModuleForm

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
    if request.method == "POST":
        form = ModuleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describle = form.cleaned_data['describle']
            project = form.cleaned_data['project']
            #保存更新
            Module.objects.create(project=project,name=name,describle=describle)
        else:
            print("创建失败")
        return HttpResponseRedirect('/module/')

@login_required()
def edit_module(request,mid):
    '''
    编辑项目
    :param request:
    :return:
    '''
    if request.method == "GET":
        module = Module.objects.get(id=mid)
        form = ModuleForm(instance=module)
        return render(request, "module_manage.html", {"type":"edit",
                                                       "form":form,
                                                       "mid":mid
                                                       })
    elif request.method == "POST":
        form = ModuleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describle = form.cleaned_data['describle']
            project = form.cleaned_data['project']
            #保存更新
            p = Module.objects.get(id=mid)
            p.project = project
            p.name = name
            p.describle = describle
            p.save()
        return HttpResponseRedirect('/module/')

@login_required()
def delete_module(request, mid):
    '''
    删除项目
    '''
    if request.method == "GET":
        try:
            module = Module.objects.get(id=mid)
        except module.DoseNotExist:
            return HttpResponseRedirect('/delete_module/')
        else:
            module.delete()
        return HttpResponseRedirect('/module/')
    else:
        return HttpResponseRedirect('/module/')
