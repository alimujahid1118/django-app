from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from blogs.models import Categories, Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, BlogForm, UserForm, EditUserForm
from django.utils.text import slugify
from django.contrib.auth.models import User

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

def blog(request):
    template = loader.get_template("blog.html")
    all_blogs = Blog.objects.all()
    context = {
        'all_blogs' : all_blogs,
    }
    return HttpResponse(template.render(context, request))

def add_blog(request):
    template = loader.get_template("add_blog.html")
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog')
        else:
            print(form.errors)
    else:
        form = BlogForm()
    context = {
        'form' : form
    }
    return HttpResponse(template.render(context, request))

def edit_blog(request, slug):
    template = loader.get_template("edit_blog.html")
    blog = get_object_or_404(Blog, slug=slug)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES ,instance=blog)
        if form.is_valid():
            post = form.save(commit=False)
            base_slug = slugify(form.cleaned_data['title'])
            slug = base_slug
            counter = 1
            while Blog.objects.filter(slug=slug).exclude(id = blog.id).exists():
                slug = f"{base_slug}-{counter}"
                counter +=1
            post.slug = slug
            post.save()
            print(post)
            return redirect('blog')
        else:
            print(form.errors)
    else:
        form = BlogForm(instance=blog)
    context = {
        'form' : form,
        'blog' : blog,
    }
    return HttpResponse(template.render(context, request))

def delete_blog(request, id):
    blog = get_object_or_404(Blog, id = id)
    blog.delete()
    return redirect('blog')

def users(request):
    template = loader.get_template("users.html")
    users = User.objects.all()
    context = {
        'users' : users
    }
    return HttpResponse(template.render(context, request))

def add_user(request):
    template = loader.get_template("add_user.html")
    form = UserForm()
    context = {
        'form' : form
    }
    return HttpResponse(template.render(context, request))

def edit_user(request, username):
    template = loader.get_template("edit_user.html")
    user = get_object_or_404(User, username = username)
    if request.method == 'POST':
        form = EditUserForm(request.POST ,instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = EditUserForm(instance=user)
    context = {
        'form' : form,
        'user' : user
    }
    return HttpResponse(template.render(context, request))

def delete_user(request, id):
    user = get_object_or_404(User, id = id)
    user.delete()
    return redirect('users')