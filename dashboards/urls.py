from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("categories/", views.categories, name="categories"),
    path("categories/add/", views.add_category, name="add_category"),
    path("categories/edit/<str:category_name>/", views.edit_category, name="edit_category"),
    path("categories/delete/<str:category_name>/", views.delete_category, name="delete_category"),
    path("blogs/", views.blog, name="blog"),
    path("blogs/add/", views.add_blog, name="add_blog"),
    path("blogs/delete/<int:id>/", views.delete_blog, name="delete_blog"),
    path("blogs/edit/<slug:slug>/", views.edit_blog, name="edit_blog"),
    path("users/", views.users, name="users"),
    path("users/add/", views.add_user, name="add_user"),
    path("users/edit/<str:username>/", views.edit_user, name="edit_user"),
    path("users/delete/<int:id>/", views.delete_user, name="delete_user"),
]