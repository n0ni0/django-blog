from django.shortcuts import render, get_object_or_404

from .models import Post


def index(request):
    posts = Post.objects.order_by('-created')
    context = {'posts': posts}
    return render(request, 'app/index.html', context)


def single_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'app/single_post.html', {'post': post})