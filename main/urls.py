from django.urls import path
from . import views

app_name='main'
urlpatterns =[
    path('', views.index, name="index"),
    path('simbathon/', views.simbathon, name="simbathon"),
    path('process/', views.process, name="process"),
    path('judge/', views.judge, name="judge"),
    path('reward/', views.reward, name="reward"),
    path('developer/', views.developer, name="developer"),
    path('dgulion/', views.dgulion, name="dgulion"),
]