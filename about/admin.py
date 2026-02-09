from django.contrib import admin
from about.models import About

@admin.register(About)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('description', 'author')

    def has_add_permission(self, request):
        count = About.objects.count()
        if count > 0:
            return False
        return True