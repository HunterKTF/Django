from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    name = request.GET.get("name") or "World"
    return HttpResponse(f'Hello, {name}!')


def login(request):
    return HttpResponse("Login Page")


def register(request):
    return HttpResponse("Register Page")
