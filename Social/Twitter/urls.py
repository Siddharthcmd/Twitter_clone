from django.urls import path
from .views import *

urlpatterns = [
    path('api/tweets/', TweetListAPIView.as_view(), name='tweet-list'),
    path('api/tweets/create/', TweetCreateAPIView.as_view(), name='tweet-create'),
    path('api/profiles/', ProfileListAPIView.as_view(), name='profile-list'),
    path('api/profiles/<int:pk>/', UserProfileAPIView.as_view(), name='user-profile'),
    path('api/tweets/<int:pk>/like/', TweetLikeToggleAPIView.as_view(), name='tweet-like-toggle'),
    path('api/profiles/<int:pk>/follow/', ProfileFollowToggleAPIView.as_view(), name='profile-follow-toggle'),
    path('api/profiles/<int:pk>/follows/', ProfileFollowAPIView.as_view(), name='profile-follow'),
    path('api/tweets/<int:pk>/delete/', TweetDeleteAPIView.as_view(), name='tweet-delete'),
    path('api/tweets/<int:pk>/update/', TweetEditAPIView.as_view(), name='tweet-update'),
]