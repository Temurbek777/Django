from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cards', views.Card, name='cards'),
    path('profile', views.Profile, name='profile'),
    path('register', views.Register, name='register'),
    path('login', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),
    path('post/<int:pk>', views.Post, name="post")
]
