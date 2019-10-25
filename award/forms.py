from .models import Project,Profile
from django import forms

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user']

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','user_project']        