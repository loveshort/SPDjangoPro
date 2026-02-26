from django.urls import path
from . import views
app_name = 'login'

urlpatterns = [
    #登录视图
    path('login_view',views.login_view,name='login_view'),
    #注册视图
    path('register',views.register,name='register'),
    #注销视图
    path('logout_view',views.logout_view,name='logout_view'),
    #个人中心视图
    path('profile_view',views.profile_view,name='profile_view'),
    # Token 验证
    path('verify_token', views.verify_token, name='verify_token'),
    #设置视图
    path('settings_view',views.settings_view,name='settings_view'),
]