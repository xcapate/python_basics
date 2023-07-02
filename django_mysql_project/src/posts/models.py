from django.db import models
from datetime import datetime
# Create your models here.
class Posts(models.Model):
    title=models.CharField(max_length=200, null=True)
    body=models.TextField(null=True)
    author=models.CharField(max_length=60, null=True)
    created_at=models.DateTimeField(default=datetime.now, blank=True)

    def getPosts():
        return Posts.objects.all()

    def getPostById(id):
        return Posts.objects.get(id=id)