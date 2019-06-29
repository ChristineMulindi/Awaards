from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Project,Profile,DesignRating,UsabilityRating,ContentRating
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    posts= Project.objects.all()

    return render(request, 'index.html')