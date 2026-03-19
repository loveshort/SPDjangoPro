from django.urls import path
from . import views

app_name = 'shopping_mine'

urlpatterns = [
    # 购物商城-我的视图
    path('shopping_mine_view/', views.shopping_mine_view, name='shopping_mine_view'),
]