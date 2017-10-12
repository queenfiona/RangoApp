from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request,'rango/index.html',{"boldmessage": "I am a bold text from index"})

def about(request):
	return render(request,'rango/about.html',{"aboutmessage" : "This is the about text from the about view"})