from django.db import models
from django.utils import timezone
# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=20, blank=False)

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name 

class Category(models.Model):
    name = models.CharField(max_length=40)

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    category = models.ForeignKey('blog.Category')
    status = models.ForeignKey('blog.Status')

    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    reject_text = models.TextField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.status = Status.objects.get(pk=2)
        self.save()

    def reject(self, param):
        self.reject_text = param
        self.save()

    def __str__(self):
        return self.title
