from django.contrib import admin
from django.contrib.auth.admin import Group, User
from .models import Profile,Tweet
# unregister Groups
admin.site.unregister(Group)
#mix prfile with user
class ProfileInline(admin.StackedInline):
    model=Profile
# extend User model
class UserAdmin(admin.ModelAdmin):
    model=User
    #just display username fields on admin page
    fields=["username"]
    inlines=[ProfileInline]

# unregister initial User
admin.site.unregister(User)
# register new User
admin.site.register(User, UserAdmin)

#regiter tweet
admin.site.register(Tweet)