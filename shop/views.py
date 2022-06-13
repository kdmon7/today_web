from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializers import *
from .models import *


def index(request):
    return render(request, 'index.html')


def products(request):
    return render(request, 'products.html')


def shop(request):
    return render(request, 'shop.html')


def products_list(request):
    return render(request, 'products_list.html')


def products_def(request):
    return render(request, 'products_def.html')


def products_write(request):
    return render(request, 'products_write.html')


def products_edit(request):
    return render(request, 'products_edit.html')


def myinfo(request):

    return render(request, 'myinfo.html')


def login(request):

    return render(request, 'login.html')


def register(request):

    return render(request, 'register.html')


class CustomUserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = member.objects.all()