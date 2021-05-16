from django.shortcuts import render

def main(request):
    return render(request, 'ideathon/main.html')

def single_post(request):
    return render(request, 'ideathon/single-post.html')