from django.shortcuts import render
from django.http import HttpResponse
from ..models import Posts


# Create your views here.
def index(request):
    posts=Posts.getPosts()
    context={
        'title':'Contract Room',
        'posts':posts
    }
    return render(request,'posts/index.html',context)

def details(request,id):
    post=Posts.getPostById(id)
    context = {
        'post':post
    }
    return render(request,'posts/details.html',context)


def handle_404_error(request,exception):
    return render(request,'error_pages/404.html')



def handle_500_error(request):
    return render(request,'error_pages/500.html')