from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Category,Page
from .forms import CategoryForm, PageForm

def index(request):
    context_dict={}
    try:
        # The inclusion of '-' sorts the values in descending order
        category_list=Category.objects.order_by('-likes')[:5]
        context_dict['categories']=category_list

        page_list=Page.objects.order_by('-views')[:5]
        context_dict['pages']=page_list
    except Exception as e:
        raise e
    
    return render(request, 'rango/index.html',context_dict)

def about(request):
	return render(request,'rango/about.html',{"aboutmessage" : "This is the about text from the about view"})

def category(request,category_name_slug):
	# Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        context_dict['category_name_slug']=category.slug

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'rango/category.html', context_dict)

def page(request,page_name_slug):
    context_dict={}
    try:
        pages=Category.objects.get(slug=page_name_slug)
        context_dict['page_title'] =pages.title
        context_dict['pages']=pages
    except Page.DoesNotExist:
        pass

    return render(request,'rango/page.html',context_dict)

def add_category(request):
    if request.method == 'POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            # Now call the index() view.The user will be shown the homepage.
            return HttpResponseRedirect('/rango/')
        else:
            print (form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form=CategoryForm()

    return render(request,'rango/add_category.html',{'form' : form})

def add_page(request, category_name_slug):

    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
                cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()
                # probably better to use a redirect here.
                return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict = {'form':form, 'category': cat}

    return render(request, 'rango/add_page.html', context_dict)
