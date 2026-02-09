from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from blogs.models import Blog
from about.models import About

def home_blog(request):
    featured_posts = Blog.objects.filter(is_featured = True, status = "Published").order_by('-created_timestamp')
    normal_posts = Blog.objects.all().filter(is_featured=False, status = "Published").order_by('-created_timestamp')
    context = {
        'featured_posts' : featured_posts,
        'normal_posts' : normal_posts,
    }
    template = loader.get_template('home-blogs.html')
    return HttpResponse(template.render(context, request))