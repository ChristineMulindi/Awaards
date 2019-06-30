from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Project,Profile,DesignRating,UsabilityRating,ContentRating
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProfileForm,ProjectForm

# Create your views here.

def home(request):
    return render(request, 'index.html')


@login_required(login_url='/accounts/login/')
def profile(request, id):
    user = User.objects.get(id=id)
    current_user = request.user
    images = Project.objects.filter(user_id = id)
    

    try:
        profile = Profile.objects.get(user_id=id)
    except ObjectDoesNotExist:
        return redirect(update_profile, current_user.id)   
    else:
    
        return render(request, 'profile.html',{"user":user, "images":images, "profile":profile})


@login_required(login_url='/accounts/login/')
def update_profile(request,id): 
    current_user = request.user
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user_id =id
            profile.save()
        return redirect(home)

    else:
        form = ProfileForm()
    return render(request, 'update_profile.html', {"user": user, "form": form})  



def search_by_site(request):
    project = Project.objects.all
    print(project)
    if 'site_name' in request.GET and request.GET["site_name"]:
        search_term = request.GET.get("site_name")
        print(search_term)
        searched_projects= Project.objects.filter(site_name__icontains=search_term)
        print(searched_projects)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"site_name": searched_projects,"project":project})

    else:
        message = "You haven't searched for any project"
        return render(request, 'search.html',{"message":message})

