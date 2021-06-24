from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from ideathon.models import Post, Comment
from hackerthon.models import Result


def mypage(request):
  user = request.user
  posts = Post.objects.filter(writer=user)
  comments = Comment.objects.filter(writer=user)
  results = Result.objects.filter(writer=user)
  return render(request, 'users/mypage.html', {'user':user, 'posts':posts, 'comments':comments, 'results':results})