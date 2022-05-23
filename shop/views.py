from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def post_view(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {"posts": posts})
