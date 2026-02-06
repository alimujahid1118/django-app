from django.urls import path
from . import views

urlpatterns = [
    path("<str:category_name>/", views.posts_by_category, name="posts_by_category" )
]