from django.shortcuts import render,redirect
from .models import Post

def main(request):
    return render(request, 'ideathon/main.html')

def single_post(request):
    return render(request, 'ideathon/single-post.html')


def new(request):
    return render(request, 'ideathon/new.html')
    
def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.category = request.POST['category']
    new_post.content = request.POST['content']
    new_post.medaifile = request.POST['mediafile']
    new_post.save()
    return redirect('ideathon:main')  