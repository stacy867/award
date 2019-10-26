from .models import Project,Profile
from django import forms
from django.forms import ModelForm

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user']

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','user_project']


class VoteForm(ModelForm):
    class Meta:
        model = Project
        fields = ('design','usability','content')

