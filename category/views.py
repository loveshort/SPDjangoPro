from django.shortcuts import render
from django.http import JsonResponse
from .models import Category

# Create your views here.
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/category_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    return render(request, 'category/category_detail.html', {'category': category})

def category_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        Category.objects.create(name=name, description=description)
        return JsonResponse({'code': 200, 'msg': '分类创建成功'})
    return render(request, 'category/category_create.html')

def category_update(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category.name = name
        category.description = description
        category.save()
        return JsonResponse({'code': 200, 'msg': '分类更新成功'})
    return render(request, 'category/category_update.html', {'category': category})

def category_delete(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return JsonResponse({'code': 200, 'msg': '分类删除成功'})