from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    #created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True, blank=True)
    content = models.TextField()

    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment')
    content = models.TextField()

    def __str__(self) -> str:
        return self.content