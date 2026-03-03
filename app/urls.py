from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

# 注册视图集
router = DefaultRouter()
router.register(r'book', views.BookList, basename='book')

urlpatterns = [
    path('app_index', views.index, name="app_index"),
    path('add_book',views.add_book,name="app_add_book"),
    path('book_detail',views.book_detail,name="book_detail"),
    path('update_book',views.update_book,name="update_book"),
]

