from django.urls import path
from .views import TweetListAPIView, TweetCreateAPIView, ProfileListAPIView, UserProfileAPIView, TweetLikeToggleAPIView

urlpatterns = [
    path('api/tweets/', TweetListAPIView.as_view(), name='tweet-list'),
    path('api/tweets/create/', TweetCreateAPIView.as_view(), name='tweet-create'),
    path('api/profiles/', ProfileListAPIView.as_view(), name='profile-list'),
    path('api/profiles/<int:pk>/', UserProfileAPIView.as_view(), name='user-profile'),
    path('api/tweets/<int:pk>/like/', TweetLikeToggleAPIView.as_view(), name='tweet-like-toggle'),
    # Other API URLs go here...
]