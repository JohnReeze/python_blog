#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render_to_response
from blog.models import Post, Status, Category

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


def index(request):
    posts = Post.objects.filter(status=Status.objects.get(pk=1)).filter(published_date__lte=timezone.now()).order_by(
        'published_date')
    categories = Category.objects.all()
    return render(request, 'blog/list.html', {'posts': posts, 'categories': categories})

def user_creation(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('django.contrib.auth.views.login')
    else:
        form = UserCreationForm()
    return render(request, 'blog/user_creation.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(status=Status.objects.get(pk=1)).filter(Q(reject_text__isnull=True) |
                                                                        Q(reject_text='')).order_by('created_date')
    categories = Category.objects.all()
    return render(request, 'blog/post_draft_list.html', {'posts': posts, 'categories': categories})


# @login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            if post.author.is_superuser:
                post.published_date = timezone.now()
                post.status = Status.objects.get(pk=1)
            else:
                post.status = Status.objects.get(pk=2)
            post.save()
            return redirect('blog.views.index')
    else:
        form = PostForm()
    return render(request, 'blog/index.html', {'form': form})





