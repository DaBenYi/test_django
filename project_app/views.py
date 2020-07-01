from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project_app.models import Project
from project_app.forms import ProjectForm

#登录成功首页面，默认项目管理页面
@login_required()#限制某个试图函数直接登录，必须经过登录才能访问
def project_manage(request):
    '''
    登录成功的首页面
    :param request:
    :return:
    '''
    project_all = Project.objects.all()#获取项目数据
    return render(request, "project_manage.html", {"projects":project_all
                                                   ,"type":"list"})
@login_required()
def add_project(request):
    '''
    创建项目
    :param request:
    :return:
    '''
    if request.method == "GET":
        return render(request, "project_manage.html", {"type":"add"})
    elif request.method == "POST":
        project_name = request.POST.get("project_name", "")
        project_describle = request.POST.get("project_describle", "")
        status = request.POST.get("status", "")
        if project_name == "":
            return render(request, "project_manage.html", {"type":"add","name_error":"项目名称不能为空"})
        Project.objects.create(name=project_name,describle=project_describle,status=status)
        return HttpResponseRedirect('/project/')

@login_required()
def edit_project(request,pid):
    '''
    编辑项目
    :param request:
    :return:
    '''
    if request.method == "GET":
        pro = Project.objects.get(id=pid)
        form = ProjectForm(instance=pro)
        return render(request, "project_manage.html", {"type":"edit",
                                                       "form":form,
                                                       "pid":pid
                                                       })
    elif request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describle = form.cleaned_data['describle']
            status = form.cleaned_data['status']
            #保存更新
            p = Project.objects.get(id=pid)
            p.status = status
            p.name = name
            p.describle = describle
            p.save()
        return HttpResponseRedirect('/project/')

@login_required()
def delete_project(request,pid):
    '''
    删除项目
    '''
    if request.method == "GET":
        try:
            project = Project.objects.get(id=pid)
        except Project.DoseNotExist:
            return HttpResponseRedirect('/project/')
        else:
            project.delete()
        return HttpResponseRedirect('/project/')
    else:
        return HttpResponseRedirect('/project/')

