from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from ..models import Posts
from datetime import datetime

# Create your views here.
def index(request):
    posts=Posts.getPosts()
    
    names = ['John','Peter','Carlos','Mike']

    names.append("Maximillian")
    names.insert(3,"Dionisius")
    names.__contains__(2);
    context = {
        'title': 'Latest posts',
        'posts':posts
    }
    #template=loader.get_template('posts/index.html')
    #return HttpResponse(template.render(context,request))
    return render(request,'posts/index.html',context)

def details(request,id):
    try:
        post = Posts.getPostById(id)
        context = {
            'post': post
        }
        
        return render(request,'posts/details.html',context)
    except TypeError:
        context={
            'error':'Oops something went wrong, please try again later!'
        }
        return render(request,'posts/oops.html',context)



