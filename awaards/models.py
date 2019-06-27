from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    
    profile_pic = models.ImageField(upload_to = 'images/',default='images/default.jpg')
    bio = models.TextField()
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @property
    def image(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url

    @classmethod
    def search_by_username(cls,search_term):
        search_result = cls.objects.filter(username__icontains=search_term)
        return search_result

    def save_profile(self):
        self.save()


    def delete_profile(self):
        self.delete()


class Project(models.Model):
    site_name = models.CharField(max_length=300)
    url = models.URLField(max_length=300)
    description =  models.CharField(max_length=300)
    technologies = models.CharField(max_length=300)
    designer = models.CharField(max_length=300)
    screenshot = models.ImageField(upload_to='images/', null=True)
    user = models.ForeignKey(User, null=True)
    user_profile=models.ForeignKey(Profile, null=True)



