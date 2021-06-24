from django.urls import path
from . import views
# from .views import *

app_name='hackerthon'
urlpatterns =[
    path('', views.main, name="main"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('<int:id>/', views.detail, name="detail"),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
]