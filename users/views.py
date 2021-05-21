from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from ideathon.models import Post


def mypage(request):
  user = request.user
  posts = Post.objects.filter(writer=user)
  return render(request, 'users/mypage.html', {'user':user, 'posts':posts})