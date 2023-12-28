from django.urls import path, include # new
from . import views

urlpatterns = [
    path('', views.home, name="home"), # new
    path('profile_list/', views.profile_list, name="profile_list"), # new
    path('profile/<int:pk>/', views.profile, name="profile"), # new
    path('login/', views.login_user, name="login"), # new
    path('logout/', views.logout_user, name="logout"), # new
    path('register/', views.register_user, name="register"), # new
    path('update_user/', views.update_user, name="update_user"), # new
    path('tweet_like/<int:pk>/', views.tweet_like, name="tweet_like"), # new
]
