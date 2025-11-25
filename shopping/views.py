from django.shortcuts import render,HttpResponse

# Create your views here.
def book_detail_query_string(request):
    book_id = request.GET.get("id")
    name = request.GET.get("name")
    return HttpResponse(f"您查找的图书id是:{book_id} 书的名字:{name}")


def book_detail_path(request,book_id):
   return HttpResponse(f"你查找的图书id是:{book_id}")

def book_detail_str(request,book_id):
    return HttpResponse(f'你查找的图书id是:{book_id}')

def book_detail_slug(request,book_id):
    return HttpResponse(f"你查找的图书id是:{book_id}")
