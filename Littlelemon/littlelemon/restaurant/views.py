from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def sayHello(request):
 return HttpResponse('Hello World')

#The views for the html file in the template 
def index(request):
 return render(request, 'index.html', {})