from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def movie_list(request):
    return HttpResponse("电影列表")

def movie_detail(request,movie_id):
    return HttpResponse(f"电影详情页的{movie_id}")
