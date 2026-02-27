from django.urls import path
from . import views

app_name = 'shopping'

urlpatterns = [
    #购物车列表视图
    path('shopping_list', views.shopping_list, name='shopping_list'),
    #购物车详情视图
    path('shopping_detail/<int:shopping_id>/', views.shopping_detail, name='shopping_detail'),
    #购物车添加视图
    path('shopping_add/', views.shopping_add, name='shopping_add'),
    #购物车删除视图
    path('shopping_delete/<int:shopping_id>/', views.shopping_delete, name='shopping_delete'),
    #购物车修改视图
    path('shopping_update/<int:shopping_id>/', views.shopping_update, name='shopping_update'),
]