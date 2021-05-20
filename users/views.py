from django.shortcuts import render, get_object_or_404
from .models import User

def mypage(request):
  return render(request, 'users/mypage.html')