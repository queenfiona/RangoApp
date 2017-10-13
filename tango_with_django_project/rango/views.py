from django.shortcuts import render
from rango.models import Category

def index(request):
	category_list=Category.objects.order_by('-likes')[:5]
	return render(request,'rango/index.html',{"categories": category_list})

def about(request):
	return render(request,'rango/about.html',{"aboutmessage" : "This is the about text from the about view"})