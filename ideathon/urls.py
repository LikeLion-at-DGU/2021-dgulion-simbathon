from django.urls import path
from . import views

app_name='ideathon'
urlpatterns =[
    path('', views.main, name="main"),
    path('', views.single_post, name="single_post"),
]