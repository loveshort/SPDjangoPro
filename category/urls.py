from django.urls import path
from . import views


app_name = 'category'

urlpatterns = [
    path('category_list', views.category_list, name='category_list'),
    path('category_detail/<int:category_id>/', views.category_detail, name='category_detail'),
    path('category_create/', views.category_create, name='category_create'),
    path('category_update/<int:category_id>/', views.category_update, name='category_update'),
    path('category_delete/<int:category_id>/', views.category_delete, name='category_delete'),
]