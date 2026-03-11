from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'shopping_login'

router = DefaultRouter()
router.login(r'shopping_login', views.ShoppingLoginModel, basename='shopping_login')

urlpatterns = [
    # 购物商城-登录视图
    path('shopping_login_view/', views.ShoppingLoginModel, name='shopping_login_view'),
    # 购物商城-注册视图
    path('shopping_register_view/', views.shopping_register_view, name='shopping_register_view'),
]