from django.db import models
from django.contrib.auth.models import User

class About(models.Model):
    description = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    github = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "About"

    def __str__(self):
        return self.description