from django.db import models
from datetime import datetime

# Create your models here.
class Posts(models.Model):
    title= models.CharField(max_length=200,null=True)
    body= models.TextField(null=True)
    created_at= models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural="Posts"
    
    def getPosts():
        posts = Posts.objects.all()[:10]
        return posts

    def getPostById(id):
        try:
            post = Posts.objects.get(id=id)
            return post
        except ValueError:
            return None