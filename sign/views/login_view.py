from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models.project import Project


# Create your views here.
#登录
def index(request):
    if request.method == "GET":
        return render(request, "index.html")
    else:
        if request.method == "POST":
            username = request.POST.get("username", "")
            password = request.POST.get("password", "")
            #authenticate函数认证给出的用户名和密码，在正确的情况下返回一个user对象
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)#登录,login函数接收httprequest对象和一个user对象
                return HttpResponseRedirect('/project/')#路径重定向
            else:
                return render(request, "index.html", {"error": "用户或密码错误！！！"})
#处理用户退出
def logout(request):
    auth.logout(request)#退出
    return HttpResponseRedirect('/index/')#重定向到登录路径






