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

def shopping_list(request):
    return render(request, 'shopping/shopping_list.html')

def shopping_detail(request, shopping_id):
    return render(request, 'shopping/shopping_detail.html', {'shopping_id': shopping_id})

def shopping_add(request):
    return render(request, 'shopping/shopping_add.html')

def shopping_delete(request, shopping_id):
    return render(request, 'shopping/shopping_delete.html', {'shopping_id': shopping_id})

def shopping_update(request, shopping_id):
    return render(request, 'shopping/shopping_update.html', {'shopping_id': shopping_id})