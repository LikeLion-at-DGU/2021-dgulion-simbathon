from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    POST_CATEGORY_CHOICES = [
        ('hi-sw', 'hi-sw'),
        ('club', 'club'),
    ]

    category = models.CharField(choices=POST_CATEGORY_CHOICES, max_length=300)
    title = models.CharField(max_length=50)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    mediafile = models.FileField(upload_to='mediafiles/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    def file_name(self):
        return self.mediafile.name[11:].split('.')[-2]
    
    def file_type(self):
        return self.mediafile.name.split('.')[-1]

class Comment(models.Model):
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now = True)
  writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')