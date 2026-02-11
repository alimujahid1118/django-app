from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from blogs.models import Categories, Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm

@login_required(login_url="login")
def dashboard(request):
    template = loader.get_template("dashboard.html")
    category_count = Categories.objects.all().count()
    blogs_count = Blog.objects.all().count()
    context = {
        'category_count' : category_count,
        'blogs_count' : blogs_count
    }
    return HttpResponse(template.render(context, request))

def categories(request):
    template = loader.get_template("categories.html")
    context = {

    }
    return HttpResponse(template.render(context, request))

def add_category(request):
    template = loader.get_template("add_category.html")
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()
    context = {
        'form' : form
    }
    return HttpResponse(template.render(context, request))

def edit_category(request, category_name):
    template = loader.get_template("edit_category.html")
    category = get_object_or_404(Categories, category_name__iexact=category_name)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm(instance=category)
    context = {
        'form' : form,
        'category' : category
    }
    return HttpResponse(template.render(context, request))

def delete_category(request, category_name):
    category = get_object_or_404(Categories, category_name__iexact = category_name)
    category.delete()
    return redirect('categories')