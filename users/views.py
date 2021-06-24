from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from ideathon.models import Post, Comment
from hackerthon.models import *


def mypage(request):
  user = request.user
  posts = Post.objects.filter(writer=user)
  comments = Comment.objects.filter(writer=user)
  try:
    member = Member.objects.get(member=user.last_name + user.first_name)
    return render(request, 'users/mypage.html', {'user':user, 'posts':posts, 'comments':comments, 'member':member})
  except Member.DoesNotExist:
    return render(request, 'users/mypage.html', {'user':user, 'posts':posts, 'comments':comments})