from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    #create relationship (dont inherit from user!)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # add any aditional attributes you want

    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to = 'profile_pics',blank = True)

    def __str__(self):
        # built in attribute of django.contrib.auth.models.User!
        return self.user.username