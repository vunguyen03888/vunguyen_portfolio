from django.urls import path, include
from .import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog_single/<int:id>', views.blog_single, name='blog_single'),
]