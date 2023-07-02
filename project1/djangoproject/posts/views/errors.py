from django.shortcuts import render
from django.http import HttpResponse

def http_response_404(request,exeption):
    return render(request,'posts/404.html')

def http_response_500(request):
    return render(request,'posts/oops.html')