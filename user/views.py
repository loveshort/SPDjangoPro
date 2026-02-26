from django.shortcuts import render
from .models import User
from django.http import JsonResponse

# Create your views here.
def user_info(request):
    #获取用户信息
    user_info = User.objects.all()
    print(user_info);
    return render(request, 'user/user.html', {'user_info': user_info})

#添加用户视图
def add_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        avatar = request.POST.get('avatar')
        user = User.objects.create(username=username, email=email, password=password, gender=gender, age=age, phone=phone, address=address, avatar=avatar)
        user.save()
        return JsonResponse({'code': 200, 'msg': '用户添加成功'});

    return render(request, 'user/add_user.html')

#编辑用户视图
def edit_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.password = request.POST.get('password')
        user.gender = request.POST.get('gender')
        user.age = request.POST.get('age')
        user.phone = request.POST.get('phone')
        user.address = request.POST.get('address')
        user.avatar = request.POST.get('avatar')
        user.save()
        return JsonResponse({'code': 200, 'msg': '用户编辑成功'})
    return render(request, 'user/edit_user.html', {'user': user})
#删除用户视图
def delete_user(request, user_id):
        user = User.objects.get(id=user_id)
        user.delete()
        return JsonResponse({'code': 200, 'msg': '用户删除成功'});
    

#用户列表视图
def user_list(request):
    users = User.objects.all()
    return render(request, 'user/user_list.html', {'users': users})

#用户详情视图   
def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'user/user_detail.html', {'user': user})