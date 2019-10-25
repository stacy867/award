from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import NewProjectForm,NewProfileForm
from .models import Project,Profile 

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer




class ProfileList(APIView):
    def get(self, request, format=None):
        profile = Profile.objects.all()
        serializers = ProfileSerializer(profile, many=True)
        return Response(serializers.data)

class ProjectList(APIView):
    def get(self, request, format=None):
        project = Project.objects.all()
        serializers = ProjectSerializer(project, many=True)
        return Response(serializers.data)        

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):

    project=Project.objects.all()

    return render(request, 'index.html',{"project":project})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('welcome')
        # return render(request, 'all-apps/post.html')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})


@login_required(login_url='/accounts/login/')
def search_results(request):
   if 'title' in request.GET and request.GET["title"]:
       search_term = request.GET.get("title")
       searched_projects = Project.search_project(search_term).all()
       current_user = request.user
    #    profile=Profile.objects.filter(user=current_user).first()
       print(searched_projects)
       message = f"{search_term}"
       return render(request, "all-apps/search.html",{"message":message,"titles": searched_projects})
   else:
       message = "You haven't searched for any term"
       return render(request, 'all-apps/search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def profile(request):
     current_user= request.user
     project=Project.objects.filter(user=current_user).all()
     profile= Profile.objects.filter(user=current_user).first()   
     return render(request,'profile.html',{"project":project,"profile":profile})       


@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('welcome')
        # return render(request, 'all-apps/post.html')

    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})



