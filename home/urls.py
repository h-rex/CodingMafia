from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("tutorials", views.tutorials, name='tutorials'),
    path("contact", views.contact, name='contact'), 
    path("html", views.html, name='html'), 
    path("css", views.css, name='css'), 
    path("js", views.js, name='js'), 
    path("python", views.python, name='python'), 
    path("blog", views.blog, name='blog'), 
    path("blog1", views.blog1, name='blog1'),
    path("blog2", views.blog2, name='blog2'), 
    path("blog3", views.blog3, name='blog3'),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    
    
]