# Twitter app model.py

from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

class Tweet(models.Model):
    body=models.CharField(max_length=140)
    created_at=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, related_name="tweets", on_delete=models.CASCADE)
    likes=models.ManyToManyField(User, related_name="likes", blank=True)

    def no_of_likes(self):
        return self.likes.count()
    def __str__(self):
        return (f"{self.user} "
                    f"{self.created_at:%Y-%m-%d %H:%M :} "
                    f"{self.body}...")

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)
    date_modified = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(blank=True, null=True, upload_to='images/')

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        # have the user follow themselves
        user_profile.follows.set([instance.profile.id])
        user_profile.save()

post_save.connect(create_profile, sender=User)
