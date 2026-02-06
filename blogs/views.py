from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Categories, Blog

def posts_by_category(request, category_name):
    template = loader.get_template('posts_by_category.html')
    #category = Categories.objects.get(category_name__iexact =category_name)
    category = get_object_or_404(Categories, category_name__iexact =category_name)
    category_id = category.id
    post_by_category = Blog.objects.filter(category = category_id, is_featured = False, status = 'Published')
    context = {
        'normal_posts' : post_by_category,
        'category_name' : category_name
    }
    return HttpResponse(template.render(context, request))