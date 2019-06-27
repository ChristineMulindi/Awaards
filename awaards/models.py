from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    site_name = models.CharField(max_length=300)
    url = models.URLField(max_length=300)
    description =  models.CharField(max_length=300)
    technologies = models.CharField(max_length=300)
    designer = models.CharField(max_length=300)
    screenshot = models.ImageField(upload_to='images/', null=True)
    user = models.ForeignKey(User, null=True)
