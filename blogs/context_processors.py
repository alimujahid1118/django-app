from .models import Categories
from about.models import About

def get_Categories(request):
    categories = Categories.objects.all()
    return dict(categories=categories)

def get_About(request):
    try:
        about = About.objects.get()
    except:
        about = None
    return dict(about=about)