from django.shortcuts import get_object_or_404, render,redirect
from .models import * # 모든 모델
from django.contrib.auth.decorators import login_required

def main(request):
    posts = Result.objects.all()
    return render(request, 'hackerthon/main.html', {'posts':posts})

@login_required
def new(request):
    return render(request, 'hackerthon/new.html')

@login_required
def create(request):
    new_post = Result()
    new_post.title = request.POST['title']
    new_post.writer = request.user
    new_post.category = request.POST['category']
    new_post.content = request.POST['content']
    new_post.team = request.POST['team']
    new_post.github = request.POST['github']
    new_post.demo = request.POST['demo']
    new_post.introduction = request.FILES.get('introduction')
    new_post.save()
    return redirect('hackerthon:main')

def detail(request, id):
    post = get_object_or_404(Result, pk=id)
    return render(request, 'hackerthon/detail.html', {'post':post}) 

@login_required
def update(request, id):
    post = get_object_or_404(Result, pk=id)
    if post.writer == request.user:
        if request.method == "POST":
            post.title = request.POST['title']
            post.content = request.POST['content']
            post.category = request.POST['category']
            post.team = request.POST['team']
            post.github = request.POST['github']
            post.demo = request.POST['demo']
            if request.FILES.get('introduction'):
                post.introduction = request.FILES.get('introduction')
            post.save()
            return redirect('hackerthon:detail', post.id)
    return render(request, 'hackerthon/update.html', {'post':post})

@login_required
def delete(request, id):
    post = get_object_or_404(Result, pk=id)
    post.delete()
    return redirect("hackerthon:main")
