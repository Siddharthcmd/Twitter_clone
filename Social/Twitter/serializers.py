from rest_framework import serializers
from .models import Tweet, Profile

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['id', 'body', 'created_at', 'user', 'likes']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'follows', 'date_modified', 'profile_image']
