from django.urls import path
from . import views

app_name='ideathon'
urlpatterns =[
    path('', views.main, name="main"),
    path('single_post/', views.single_post, name="single_post"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('<int:id>', views.detail, name="detail"),
]