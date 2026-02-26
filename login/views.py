from django.shortcuts import render
from django.http import HttpResponse
from .models import LoginModel

# Create your views here.
import uuid
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import LoginModel

# 模拟 Token 存储（实际生产中应存入数据库或 Redis）
TOKEN_STORE = {}

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = LoginModel.objects.filter(username=username, password=password).first()
        if user:
            # 生成 Token
            token = str(uuid.uuid4())
            # 存储 Token 与用户的映射
            TOKEN_STORE[token] = user.id
            return JsonResponse({'code': 200, 'msg': '登录成功', 'token': token})
        else:
            return JsonResponse({'code': 400, 'msg': '用户名或密码错误'})
    
    return render(request, 'login/login.html')

def verify_token(request):
    """
    鉴权视图：验证 Token 是否有效
    客户端需在 Header 中携带 Token: Authorization: Bearer <token>
    """
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return JsonResponse({'code': 401, 'msg': '未提供 Token'})
    
    token = auth_header.split(' ')[1]
    user_id = TOKEN_STORE.get(token)
    
    if user_id:
        user = LoginModel.objects.get(id=user_id)
        return JsonResponse({'code': 200, 'msg': 'Token 有效', 'user': user.username})
    else:
        return JsonResponse({'code': 403, 'msg': 'Token 无效或已过期'}) 

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