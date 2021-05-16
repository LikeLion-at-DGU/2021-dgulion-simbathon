from django.urls import path
from . import views

app_name='main'
urlpatterns =[
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('single_project/', views.single_project, name="single_project"),
]