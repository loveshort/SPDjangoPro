from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
# Create your views here.
from models import AppModel
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
