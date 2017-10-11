from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request,'rango/index.html',{"boldmessage": "I am a bold text from index"})

def about(request):
	return HttpResponse("Rango says this is the about page <br> <a href='/rango/'>index</a>")