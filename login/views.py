from django.shortcuts import render
from django.http import HttpResponse
from .models import LoginModel

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        # 获取用户名和密码 通过POST请求
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 存入数据库
        if LoginModel.objects.filter(username=username,password=password).exists():
            return HttpResponse(f"登录成功！用户名: {username}")
        else:
            return HttpResponse(f"登录失败！用户名或密码错误！")
    
    # 如果是GET请求，返回登录页面
    return render(request, 'login/login.html') 

def register(request):
    if request.method == 'POST':
        # 获取用户名和密码 通过POST请求
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 存入数据库
        user = LoginModel.objects.create(username=username, password=password)
        user.save()
        return HttpResponse(f"注册成功！用户名: {username}")
    
    # 如果是GET请求，返回注册页面
    return render(request, 'login/register.html')     

def logout_view(request):
    if request.method == 'POST':
        # 获取用户名和密码 通过POST请求
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 数据库中删除用户
        user = LoginModel.objects.filter(username=username, password=password).delete()
        if user:
            return HttpResponse(f"注销成功！用户名: {username}")
        else:
            return HttpResponse(f"注销失败！用户名或密码错误！")
    else:
        return render(request, 'login/logout.html')

def profile_view(request):
    return HttpResponse("个人中心视图")

def settings_view(request):
    return HttpResponse("设置视图")