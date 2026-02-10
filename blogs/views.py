from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Categories, Blog
from django.db.models import Q
from blog_main.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def posts_by_category(request, category_name):
    template = loader.get_template('posts_by_category.html')
    #category = Categories.objects.get(category_name__iexact =category_name)
    category = get_object_or_404(Categories, category_name__iexact =category_name)
    category_id = category.id
    post_by_category = Blog.objects.filter(category = category_id, status = 'Published')
    context = {
        'normal_posts' : post_by_category,
        'category_name' : category_name
    }
    return HttpResponse(template.render(context, request))

def blogs(request, slug):
    template = loader.get_template('blogs.html')
    single_blog = get_object_or_404(Blog, slug=slug, status="Published")
    context = {
        'single_blog' : single_blog,
    }
    return HttpResponse(template.render(context , request))

def search(request):
    keyword = request.GET.get('keyword')
    template = loader.get_template('search.html')
    search = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status="Published")
    context = {
        'search': search,
        'keyword': keyword
    }
    return HttpResponse(template.render(context, request))

def register(request):
    template = loader.get_template("register.html")
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = RegistrationForm()
    context = {
        'form' : form
    }
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template("login.html")
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = auth.authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if user is not None:
                auth.login(request, user)
                return redirect('/')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return HttpResponse(template.render(context, request))

def logout(request):
    auth.logout(request)
    return redirect('/')