from django.db import models

from django.db import models

class Post(models.Model):
    POST_CATEGORY_CHOICES = [
        ('hi-sw', 'hi-sw'),
        ('club', 'club'),    
    ]

    category = models.CharField(choices=POST_CATEGORY_CHOICES, max_length=300)
    title = models.CharField(max_length=50)
    content = models.TextField()
    mediafile = models.FileField(upload_to='mediafiles/')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
