from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EmployerRegisterForm, CandidateRegisterForm
from .models import EmployerProfile, CandidateProfile

def register(request):
    if request.method == 'POST':
        if 'employer' in request.POST:
            form = EmployerRegisterForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_employer = True
                user.save()
                EmployerProfile.objects.create(user=user, company_name=form.cleaned_data.get('company_name'), company_description=form.cleaned_data.get('company_description'))
                messages.success(request, f'Employer account created for {user.username}!')
                return redirect('login')
        elif 'candidate' in request.POST:
            form = CandidateRegisterForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_candidate = True
                user.save()
                CandidateProfile.objects.create(user=user, resume=form.cleaned_data.get('resume'))
                messages.success(request, f'Candidate account created for {user.username}!')
                return redirect('login')
    else:
        employer_form = EmployerRegisterForm()
        candidate_form = CandidateRegisterForm()
    return render(request, 'main/register.html', {'employer_form': employer_form, 'candidate_form': candidate_form})

@login_required
def profile(request):
    if request.user.is_employer:
        profile = EmployerProfile.objects.get(user=request.user)
    else:
        profile = CandidateProfile.objects.get(user=request.user)
    return render(request, 'main/profile.html', {'profile': profile})
