from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Post


def post_view(request):
    if request.method == 'POST':
        post = Post()
        post.post_id = request.POST['post_id']
        post.save()
        redirect('post')
    else:
        post = Post.objects.all()
        return render(request, 'index.html', {'post': post})
