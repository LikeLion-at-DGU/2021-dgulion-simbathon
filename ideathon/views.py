from django.shortcuts import get_object_or_404, render,redirect
from .models import Post

def main(request):
    posts = Post.objects.all()
    return render(request, 'ideathon/main.html', {'posts':posts})

def single_post(request):
    return render(request, 'ideathon/single-post.html')

def new(request):
    return render(request, 'ideathon/new.html')

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.category = request.POST['category']
    new_post.content = request.POST['content']
    new_post.mediafile = request.FILES['mediafile']
    new_post.save()
    return redirect('ideathon:main')

def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'ideathon/detail.html', {'post':post})