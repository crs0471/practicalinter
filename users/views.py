from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from .models import UserModel
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def register(request):
    if request.method != 'POST':
        return HttpResponseBadRequest

    email = request.POST.get('email')
    name = request.POST.get('name')
    password = request.POST.get('password')

    is_created = UserModel.objects.create(
        name=name,
        password=password,
        email=email
    )

    return JsonResponse({
        'status':'success'
    })

@csrf_exempt
def login(request):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    
    email = request.POST.get('email')
    password = request.POST.get('password')

    user_obj = UserModel.objects.filter(email=email, password=password).first()
    if user_obj:
        request.session['User'] = {
            'email' : user_obj.email,
            'name' : user_obj.name
        }
        return JsonResponse({
            'status':'success'
        })
    else:
        return JsonResponse({
            'status': 'error',
            'message': 'user not found'
        })
