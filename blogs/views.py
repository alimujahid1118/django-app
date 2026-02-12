from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Categories, Blog, Comment
from about.models import About
from .forms import CommentForm
from django.db.models import Q
from blog_main.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.models import Group

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
    single_blog = get_object_or_404(Blog, slug=slug, status="Published")
    comments = Comment.objects.filter(blog=single_blog).order_by('created_timestamp')
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = single_blog
            comment.user = request.user  # ensure user is logged in
            comment.save()
            return redirect('blogs', slug=slug)  # Redirect to the same page after comment
    else:
        form = CommentForm()

    context = {
        'single_blog': single_blog,
        'comments': comments,
        'form': form,
        'categories': Categories.objects.all(),  # Sidebar
        'about': About.objects.first()          # Sidebar
    }
    return render(request, 'blogs.html', context)

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
            user = form.save(commit=False)
            user.save()
            group = Group.objects.get(name="Editor")
            user.groups.add(group)
            user.save()
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
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return HttpResponse(template.render(context, request))

def logout(request):
    auth.logout(request)
    return redirect('/')