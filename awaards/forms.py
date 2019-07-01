from django import forms
from .models import Project,Profile,Rating
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio', 'contact']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [ 'site_name','url','description', 'technologies', 'designer', 'screenshot']


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['usability_rating', 'design_rating', 'content_rating']


