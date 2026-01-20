from django.contrib import admin
from .models import Categories, Blog

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('title',) }
    list_display = (
        'title',
        'author',
        'category',
        'status',
        'is_featured'
    )
    search_fields = ('id', 'title', 'status', 'category__category_name')
    list_editable = ('is_featured',)

admin.site.register(Categories)
admin.site.register(Blog, BlogAdmin)