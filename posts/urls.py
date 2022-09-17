from django.contrib import admin
from django.urls import path, include
from posts import views


urlpatterns = [

    path('home', views.HomeView.as_view(), name="home"),
    path('post/<int:post_id>', views.delete_post, name="delete"),
    path('post/like/<int:post_id>', views.like, name="like"),
    path('post/unlike/<int:post_id>', views.unlike, name="unlike"),

]