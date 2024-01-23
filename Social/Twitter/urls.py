from django.urls import path
from .views import *

urlpatterns = [
    path('api/tweets/', TweetListAPIView.as_view(), name='tweet-list'),
    path('api/tweets/create/', TweetCreateAPIView.as_view(), name='tweet-create'),
    path('api/profiles/', ProfileListAPIView.as_view(), name='profile-list'),
    path('api/profiles/<str:user__username>/', UserProfileAPIView.as_view(), name='user-profile'),
    path('api/tweets/like/<int:pk>/', TweetLikeToggleAPIView.as_view(), name='tweet-like-toggle'),
    path('api/profiles/follow/<str:username>/', ProfileFollowToggleAPIView.as_view(), name='profile-follow-toggle'),
    path('api/profiles/follows/<str:username>/', ProfileFollowAPIView.as_view(), name='profile-follow'),
    path('api/tweets/delete/<int:pk>/', TweetDeleteAPIView.as_view(), name='tweet-delete'),
    path('api/tweets/edit/<int:pk>/', TweetEditAPIView.as_view(), name='tweet-edit'),
]