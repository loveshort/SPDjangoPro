from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('list', views.movie_list, name='movie_list'),
    path('detail/<int:movie_id>', views.movie_detail, name='movie_detail'),
]