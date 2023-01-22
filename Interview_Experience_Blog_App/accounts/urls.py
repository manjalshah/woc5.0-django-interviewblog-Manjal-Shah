from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.LoginPage, name='login'),
    path('register/', views.RegisterPage, name='register'),
    path('logout/', views.LogoutUser, name='logout'),
    path('profile/', views.ProfilePage, name='profile')
]