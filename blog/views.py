from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
def movie_list(request):
    return HttpResponse("电影列表")

def movie_detail(request,movie_id):
    return HttpResponse(f"电影详情页的{movie_id}")

class 


class MovieList(APIView):
    def get(self, request):
        return Response("电影列表")