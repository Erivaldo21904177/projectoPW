from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=200)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = RichTextField(blank = True,null=True)


class Comment(models.Model):
    post = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.Post.title, self.name)
# Create your models here.
