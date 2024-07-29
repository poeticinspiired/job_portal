from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, EmployerProfile, CandidateProfile

class EmployerRegisterForm(UserCreationForm):
    company_name = forms.CharField(max_length=255)
    company_description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'company_name', 'company_description']

class CandidateRegisterForm(UserCreationForm):
    resume = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'resume']
