from django.shortcuts import render, get_object_or_404

from .models import Post, Category


def index(request):
    posts = Post.objects.order_by('-created')
    context = {'posts': posts}
    return render(request, 'app/index.html', context)


def single_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'app/single_post.html', {'post': post})


def show_category(request, category):
    categories = Category.objects.filter(slug=category)
    posts = Post.objects.filter(category=categories)
    return render(request, 'app/categories.html', {
        'posts': posts,
        'category': category
    })