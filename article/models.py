from django.db import models

# Create your models here.


class Article(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    body = models.TextField()


class Comment(models.Model):
    author = models.CharField(max_length=50)
    body = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
