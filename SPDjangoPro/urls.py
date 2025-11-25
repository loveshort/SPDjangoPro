"""
URL configuration for SPDjangoPro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import HttpResponse
from shopping import views

def index(request):
    return HttpResponse("欢迎来写第一节python django")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("s", index),
    path("shopping",include('shopping.urls'),name="shopping"),

    path("book",views.book_detail_query_string,name="book_detail_quer  y_string"),

    path('book/<int:book_id>',views.book_detail_path,name="book_detail_path"),

    path('book/<str:book_id>/',views.book_detail_str,name='book_detail_str'),

    path("book/<slug:book_id>/",views.book_detail_slug,name="book_detail_slug"),

   # path("blog/",include('blog.urls'),name='blog'),

    path('app/',include('app.urls'),name='app'),
]
