from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    #用户信息视图
    path('user_info/', views.user_info, name='user_info'),
    #添加用户视图
    path('add_user/', views.add_user, name='add_user'),
    #编辑用户视图
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    #删除用户视图
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    #用户列表视图
    path('user_list/', views.user_list, name='user_list'),
    #用户详情视图
    path('user_detail/<int:user_id>/', views.user_detail, name='user_detail'),
]