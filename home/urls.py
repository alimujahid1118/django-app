from . import views
from django.urls import path

urlpatterns = [
    path("", views.home_blog, name="home_blog")
]