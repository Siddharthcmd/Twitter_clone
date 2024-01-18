from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Profile, Tweet
from .serializers import TweetSerializer, ProfileSerializer
from django.contrib import messages

class TweetListAPIView(generics.ListAPIView):
    queryset = Tweet.objects.all().order_by('-created_at')
    serializer_class = TweetSerializer
    permission_classes = [IsAuthenticated]

class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class = TweetSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProfileListAPIView(generics.ListAPIView):
    def get_queryset(self):
        return Profile.objects.exclude(user=self.request.user)
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

class UserProfileAPIView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'user__id'

# Other API views go here...

class TweetLikeToggleAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        tweet = get_object_or_404(Tweet, id=pk)
        if tweet.likes.filter(id=request.user.id):
            tweet.likes.remove(request.user)
        else:
            tweet.likes.add(request.user)
        return Response({"message": "Like toggled successfully"}, status=status.HTTP_200_OK)

# Other API views go here...
