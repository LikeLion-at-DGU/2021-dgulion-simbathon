from django.urls import path
from . import views
from .views import *

app_name='ideathon'
urlpatterns =[
    path('', views.main, name="main"),
    path('single_post/', views.single_post, name="single_post"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('<int:id>/', views.detail, name="detail"),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
    #comment
    path('<int:post_id>/create_comment', create_comment, name="create_comment"),
]