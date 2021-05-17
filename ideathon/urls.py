from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='ideathon'
urlpatterns =[
    path('', views.main, name="main"),
    path('single_post/', views.single_post, name="single_post"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)