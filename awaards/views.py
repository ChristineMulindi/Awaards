from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Project,Profile,Rating
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProfileForm,ProjectForm,RatingForm
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly

# Create your views here.
@login_required(login_url='/accounts/login')
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
    if 'searchSite' in request.GET and request.GET["searchSite"]:
        search_term = request.GET.get("searchSite")
        # print(search_term)
        searched_projects= Project.objects.filter(site_name__icontains=search_term)
        print(searched_projects)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"site_name": searched_projects,"project":project})

    else:
        message = "You haven't searched for any project"
        return render(request, 'search.html',{"message":message})



@login_required(login_url='/accounts/login/')
def post_project(request,id):
    current_user = request.user
    print(current_user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user=current_user
            project.user_profile = Profile.objects.get(user_id=id)
            project.save()
        return redirect(home)

    else:
        form = ProjectForm()
    return render(request, 'post_project.html', {"user": current_user, "form": form}) 


@login_required(login_url='/accounts/login/')
def main(request,id):
    users = User.objects.all()
    current = request.user
    projects = Project.objects.all()
    return render(request,'project.html',{"users":users, "user":current, "projects":projects})


@login_required(login_url='/accounts/login/')
def project(request,id):
    current_user = request.user 
    current_project = Project.objects.get(id=id)
    ratings = Rating.objects.filter(project_id=id)
    return render(request, 'main.html', {"user": current_user, "project": current_project, "ratings":ratings}) 



@login_required(login_url='/accounts/login/')
def rating(request,id):
    current_user = request.user 
    current_project = Project.objects.get(id=id)
    print(current_project)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = current_user
            rating.project=current_project
            rating.save()
        return redirect('project',id)

    else:
        form = RatingForm()
    return render(request, 'rating.html', {"user": current_user, "project": current_project, "form": form}) 




def signout(request):
    logout(request)
    return redirect('login')


class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)
    permission_classes = (IsAdminOrReadOnly,)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

 
class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_profile(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404  

    def get(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(project, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_profile(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProjectList(APIView):
    def get(self, request, format=None):
        all_project = Project.objects.all()
        serializers = ProjectSerializer(all_project, many=True)
        return Response(serializers.data)
    permission_classes = (IsAdminOrReadOnly,)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

   
class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_project(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_project(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)












