from django.urls import path
from . import views

app_name = 'shopping_square'

urlpatterns = [
    # 购物商城-广场视图
    path('shopping_square_view/', views.shopping_square_view, name='shopping_square_view'),
]