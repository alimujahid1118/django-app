from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Categories(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name
    
STATUS_CHOICES = (
    ("Draft", "Draft"),
    ("Published", "Published")
)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150 ,unique=True, blank= True)
    category = models.ForeignKey(Categories, on_delete= models.CASCADE)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to= 'uploads/%Y/%m/%d')
    short_description = models.TextField(max_length= 500)
    blog_body = models.TextField(max_length= 2000)
    status = models.CharField(choices=STATUS_CHOICES, default="Draft")
    is_featured = models.BooleanField(default= False)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Blog.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter +=1
            self.slug = slug
        super().save(*args, **kwargs)

class Comment(models.Model):
    description = models.TextField(max_length=250)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description