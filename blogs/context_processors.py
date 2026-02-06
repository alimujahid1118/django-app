from .models import Categories

def get_Categories(request):
    categories = Categories.objects.all()
    return dict(categories=categories)