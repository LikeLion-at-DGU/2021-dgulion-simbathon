from django.shortcuts import get_object_or_404, render,redirect
from .models import * # 모든 모델
from django.contrib.auth.decorators import login_required

def main(request):
    posts = Post.objects.all()
    return render(request, 'ideathon/main.html', {'posts':posts})

def single_post(request):
    return render(request, 'ideathon/single-post.html')

@login_required
def new(request):
    return render(request, 'ideathon/new.html')

@login_required
def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.user
    new_post.category = request.POST['category']
    new_post.content = request.POST['content']
    new_post.mediafile = request.FILES.get('mediafile')
    new_post.save()
    return redirect('ideathon:main')

def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    all_comments = post.comments.all().order_by('-created_at')
    return render(request, 'ideathon/detail.html', {'post':post, 'comments':all_comments}) #html>comments

@login_required
def update(request, id):
    post = get_object_or_404(Post, pk=id)
    if post.writer == request.user:
        if request.method == "POST":
            post.title = request.POST['title']
            post.content = request.POST['content']
            post.save()
            return redirect('ideathon:detail', post.id)
    return render(request, 'ideathon/update.html', {'post':post})

@login_required
def delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect("ideathon:main")

def create_comment(request, post_id) : # 어느 게시글?
  if request.method == "POST":
    post = get_object_or_404(Post, pk=post_id)
    comment_content= request.POST.get('content') # html의 name이랑 같아!
    current_user = request.user
    Comment.objects.create(content=comment_content, post=post,  writer=current_user) # 모델 = views.py
  return redirect('ideathon:detail', post.pk)

def update_comment(request, post_id, comment_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method=="POST":
        comment.content = request.POST['content']
        comment.save()
        all_comments = post.comments.all()
        return redirect('ideathon:detail', post.pk)
    return render(request, 'ideathon/update_comment.html', {'comment' :comment})

def delete_comment(request, post_id, comment_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('ideathon:detail', post.pk)
