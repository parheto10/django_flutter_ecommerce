from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request):

    # queruset = User.objects.all()
    user:User = User.objects.get(pk=1)
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    print(username)
    print(email)
    return JsonResponse({
        'username': username,
        'email': email,
        'password': password,
    })

# Create your views here.
