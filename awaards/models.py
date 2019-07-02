from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    
    profile_pic = models.ImageField(upload_to = 'images/',default='images/default.jpg')
    bio = models.TextField()
    contact = models.TextField()
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

    def __str__(self):
        return self.site_name

    def save_project(self):
        self.save()

    def delete_project(self):
        self.save()

    @classmethod
    def retrieve_all(cls):
        all_objects = Project.objects.all()
        for item in all_objects:
            return item

    @classmethod
    def get_project_by_id(cls,id):
        project_result = cls.objects.get(id=id)
        return project_result

    @classmethod
    def update_project(cls,current_value,new_value):
        fetched_object = cls.objects.filter(designer=current_value).update(designer=new_value)
        return fetched_object     
    
    @classmethod
    def search_by_site(cls,search_term):
        search_result = cls.objects.filter(site_name__icontains=search_term)
        return search_result
        

class Rating(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6,'6'),
        (7,'7'),
        (8,'8'),
        (9,'9'),
        (10,'10')
    )
    project = models.ForeignKey(Project)
    pub_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    usability_rating = models.IntegerField(default=0, choices=RATING_CHOICES, null=True)
    design_rating = models.IntegerField(default=0, choices=RATING_CHOICES, null=True)
    content_rating = models.IntegerField(default=0, choices=RATING_CHOICES, null=True)
    review = models.CharField(max_length=300)
   
    def __str__(self):
        return self.review

    def save_rating(self):
        self.save()

    def delete_rating(self):
        self.save()

class Votes(models.Model):
    post = models.ForeignKey('Project', null=True)
    user = models.ForeignKey(User)
    profile = models.ForeignKey(Profile)
    count  = models.IntegerField()
   
