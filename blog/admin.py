
from django.contrib import admin
from blog.models import Post
from blog.models import Status
from blog.models import Category
admin.site.register(Post)
admin.site.register(Status)
admin.site.register(Category)
# Register your models here.
