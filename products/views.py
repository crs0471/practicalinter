from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .models import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add(request):
    
    title = request.POST.get('title')
    description = request.POST.get('description')
    price = request.POST.get('price')
    discount = request.POST.get('discount')
    files_data = request.FILES
    print(files_data)

    product_obj = ProductModel.objects.create(
        title=title,
        description=description,
        price=price,
        discount=discount,    
    )

    for image in files_data.get('images'):
        ProductImageModel.objects.create(
            product_id=product_obj.id,
            image=image
        )

    return JsonResponse({'status':'success'})

def list(request):
    search = request.GET.get('search')
    data = ProductModel.objects.all()
    if search:
        data = list(data.filter(title__icontains=search).values())
    else:
        data = list(data.values())
    return JsonResponse({'data':data})
