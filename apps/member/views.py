from sys import prefix
from django.shortcuts import  redirect, render
from django.views.generic import TemplateView
from apps.member.models import Role
from .forms import UserRegisterForm, HospitalRegisterForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from apps.hospital.models import Hospital, HospitalAdmin 
from common.constants import Contants

class UserRegisterPage(TemplateView):
    template_name = 'member/register.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['form'] = UserRegisterForm
        return context

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            role=Role.objects.get(name=Contants.ROLE_USER)
            user.role_assigned=role
            user.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("dashboard")
        return render(request, self.template_name, context={'form':form})
   

class UserLoginPage(TemplateView):
    template_name = 'member/login.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AuthenticationForm
        return context 

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
        return render(request, self.template_name, context={'form':form})


class HospitalLoginPage(TemplateView):
    template_name = 'member/hospital_login.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AuthenticationForm
        return context 

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
        return render(request, self.template_name, context={'form':form})


class HospitalRegisterPage(TemplateView):
    template_name = 'member/hospital_register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_admin'] = UserRegisterForm(prefix='admin')
        context['form_hospital'] = HospitalRegisterForm(prefix='hospital')
        return context 
        
    def post(self, request):
        form_hospital = HospitalRegisterForm(request.POST, request.FILES, prefix='hospital')
        form_admin = UserRegisterForm(request.POST, prefix='admin')
        if form_hospital.is_valid() and form_admin.is_valid():
            hospital=form_hospital.save()
            user=form_admin.save(commit=False)
            role=Role.objects.get(name=Contants.ROLE_HOSPITAL_ADMIN)
            user.role_assigned=role
            user.save()
            HospitalAdmin.objects.create(user=user, hospital=hospital)
            messages.success(request, "Registration successful.You can login after hospital gets approved within 4-5 working days." )
            return redirect("homepage")
        context={}
        context['form_admin'] = form_admin
        context['form_hospital'] = form_hospital
        return render(request, self.template_name, context)
      

@login_required
def logoutpage(request):
    logout(request)
    messages.success(request,'You were successfully logout.')
    return redirect("homepage")

