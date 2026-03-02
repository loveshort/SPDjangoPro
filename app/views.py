from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
# Create your views here.
from .models import AppModel

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AppSerializer
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.generics import GenericAPIView


# viewsets 视图类 - 开发
class BookList(viewsets.ModelViewSet):
    queryset = AppModel.objects.all()
    serializer_class = AppSerializer
    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)
    def put(self, request, pk):
        return self.update(request, pk)
    def delete(self, request, pk):
        return self.destroy(request, pk)
    def retrieve(self, request, pk):
        return self.retrieve(request, pk)
    def update(self, request, pk):
        return self.update(request, pk)
    def destroy(self, request, pk):
        return self.destroy(request, pk)
    def list(self, request):
        return self.list(request)
    def create(self, request):
        return self.create(request)
    def update(self, request, pk):
        return self.update(request, pk)
    def destroy(self, request, pk):
        return self.destroy(request, pk)


#mixins 视图类 - 开发
class BookList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = AppModel.objects.all()
    serializer_class = AppSerializer
    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)
    def put(self, request, pk):
        return self.update(request, pk)
    def delete(self, request, pk):
        return self.destroy(request, pk)

        

class BookList(ListCreateAPIView):
    queryset = AppModel.objects.all()
    serializer_class = AppSerializer
    def get(self, request):
        books = self.get_queryset()
        serializer = self.serializer_class(instance=books, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk):
        book = self.get_object()
        serializer = self.serializer_class(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        book = self.get_object()
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  

class BookList(RetrieveUpdateDestroyAPIView):
    queryset = AppModel.objects.all()
    serializer_class = AppSerializer
    def get(self, request, pk):
        book = self.get_object()
        serializer = self.serializer_class(instance=book)
        return Response(serializer.data)
    def put(self, request, pk):
        book = self.get_object()
        serializer = self.serializer_class(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        book = self.get_object()
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  


# GenericAPIView 视图类 - 开发
class BookList(GenericAPIView):
    queryset = AppModel.objects.all()
    serializer_class = AppSerializer
    def get(self, request):
        books = self.get_queryset()
        serializer = self.serializer_class(instance=books, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# APIView 视图类 - 开发
class BookList(APIView):
    def get(self, request):
        books = AppModel.objects.all()
        serializer = AppSerializer(instance=books, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = AppSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = AppModel.objects.all()
        serializer = AppSerializer(instance=books, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AppSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def index(request):
    #获取游标对象
    cursor = connection.cursor()
    #拿到游标对象后执行sql语句
    cursor.execute("select * from book")
    #获取所有的数据
    rows = cursor.fetchall()
    #遍历查询到的数据
    for row in rows:
        print(row)
    return HttpResponse("查询成功！")

def add_book(request):
    book = AppModel(name="那笔小新",price=10.01,author="三毛")
    book.save()
    return HttpResponse("图书插入成功")

def query_book(request):
    books = AppModel.objects.filter(name="那笔小新")
    for book in books:
        print(book.id,book.author,book.price)
    return HttpResponse("查找成功")

def query_book_get(request):
    book = AppModel.objects.get(id = 1)
    print(book.id,book.author,book.price)
    return HttpResponse("查找成功")

def order_view(request):
    books = AppModel.objects.order_by("-price")
    for book in books:
        print(book.id,book.author,book.price)
    return HttpResponse("排序成功")

def update_view(request):
    books = AppModel.objects.get(id = 1)
    books.name = "西游记"
    books.save()
    return HttpResponse("修改成功")

def delete_view(request):
    books = AppModel.objects.get(id = 1)
    books.delete()
    return  HttpResponse("删除成功")
#书名的详情页
def book_detail(request,id):
    bookId = AppModel.objects.get(id = id)
    #查询对应详情页的书，使用id查询正常的时间
    book = AppModel.objects.filter(id = bookId)
    return HttpResponse(f"详情信息${book}")
#书名的更新
def update_book(request,id):
    book = AppModel.objects.get(id = id)
    book.price = book.price + 10
    book.name = book.name + " " + book.author
    book.author = book.author + " " + book.price
    book.save()
    return HttpResponse("更新成功")


