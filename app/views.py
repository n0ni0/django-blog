from django.shortcuts import render

from .models import Post


def index(request):
    posts = Post.objects.order_by('-created')
    context = {'posts': posts}
    return render(request, 'app/index.html', context)
