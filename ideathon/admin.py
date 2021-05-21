from django.contrib import admin
from .models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'writer',
        'category',
        'mediafile',
        'created_at',
    )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display=(
    'id',
    'content',
  )    
