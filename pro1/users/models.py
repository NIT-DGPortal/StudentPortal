from django.db import models
from django.contrib.auth.models import User # used standard model

class Profile(models.Model):  # model inherited
    user = models.OneToOneField(User, on_delete = models.CASCADE); #one to one linked CASCADE =profile delete != user delete but vice versa
    # adding profile picture

    img = models.ImageField(default = 'default.jpg',upload_to='profile_pics')
    # how to print it out

    def __str__(self):
        return f'{self.user.username} Profile'
        # need to chage database changes as well
        # run terminal --> need pillow package
        # update database python manage.py migrate
        # now pass img location to render user.profile.img.url
        # if no image default.jpg
        # if different apps use different profile pics locatin conflict-- so relocate profile pics directory elsewhere
        
