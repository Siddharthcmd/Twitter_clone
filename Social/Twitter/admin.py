from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import Profile, Tweet

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ['user','body','created_at']
    list_filter = ['created_at']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','date_modified']
    list_filter = ['date_modified']
