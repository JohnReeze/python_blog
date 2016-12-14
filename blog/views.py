#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render_to_response
from blog.models import Post, Status, Category

def index(request):
    posts = Post.objects.filter(status=Status.objects.get(pk=1)).filter(published_date__lte=timezone.now()).order_by(
        'published_date')
    categories = Category.objects.all()
    return render(request, 'blog/list.html', {'posts': posts, 'categories': categories})

