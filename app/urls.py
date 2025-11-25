from django.urls import path
from . import views

urlpatterns = [
    path('app_index', views.index, name="app_index"),
    path('add_book',views.add_book,name="app_add_book"),

]

