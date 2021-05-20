from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def single_project(request):
    return render(request, 'main/single-project.html')

def simbathon(request):
    return render(request, 'main/simbathon.html')

def process(request):
    return render(request, 'main/process.html')

def judge(request):
    return render(request, 'main/judge.html')

def reward(request):
    return render(request, 'main/reward.html')

def developer(request):
    return render(request, 'main/developer.html')

def dgulion(request):
    return render(request, 'main/dgulion.html')