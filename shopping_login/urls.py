from django.urls import path
from . import views

app_name = 'shopping_login'

urlpatterns = [
    # 购物商城-登录视图
    path('shopping_login_view/', views.shopping_login_view, name='shopping_login_view'),
    # 购物商城-注册视图
    path('shopping_register_view/', views.shopping_register_view, name='shopping_register_view'),
]