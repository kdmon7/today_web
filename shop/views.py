from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Post


def post_view(request):
    #POST 방식
    if request.method == 'POST': 
        post = Post()
        post.post_id = request.POST['post_id']
        post.save()
        redirect('post')
    #GET 방식
    else:
        post = Post.objects.all()
        return render(request, 'index.html', {'post': post})
