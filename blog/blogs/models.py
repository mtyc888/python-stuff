from django.db import models

# Create your models here.
class Blog(models.Model):
    """Blog model"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text

class Post(models.Model):
    """Post model"""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    def __str__(self):
        return self.text