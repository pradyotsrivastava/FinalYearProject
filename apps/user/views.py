import json
from sre_parse import State
from urllib import request
from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic import TemplateView, UpdateView
from apps.cremation.forms import CremationForm
from apps.cremation.models import Cremation

from apps.feedback.models import FeedbackDoctor, FeedbackHospital, FeedbackNgo
from apps.home.models import City, Specialization, State
from apps.ngo.forms import FundRaiseForm
from apps.ngo.models import FundRaise, Ngo
from .forms import CustomUserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.feedback.forms import FeedbackDoctorForm, FeedbackHospitalForm, FeedbackNgoForm
# Create your views here.

class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'user/dashboard.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        stateCity = dict()
        for obj in City.objects.all():
            stateCity.setdefault(str(obj.state.name), []).append(obj.name)
        states=[]
        for obj in State.objects.all():
            states.append(obj.name)
        category_sp=[]
        for obj in Specialization.objects.all():
            category_sp.append(obj.name)
        category_ngo=[]
        for obj in Ngo.objects.all():
            category_ngo.append(obj.purpose)
        context['stateCity']=json.dumps(stateCity)
        context['states']=json.dumps(states)
        context['category_sp']=json.dumps(category_sp)
        context['category_ngo']=json.dumps(category_ngo)
        
        context['fundraise_stats']=FundRaise.objects.filter(user=self.request.user).count()
        context['cremation_stats']=Cremation.objects.filter(user=self.request.user).count()
        f_ngo=FeedbackNgo.objects.filter(user=self.request.user).count()
        f_doc=FeedbackDoctor.objects.filter(user=self.request.user).count()
        f_hos=FeedbackHospital.objects.filter(user=self.request.user).count()
        context['feedback_stats']=f_ngo+f_doc+f_hos
        return context

    # def post(self, request):
    #     form = UserRegisterForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         login(request, user)
    #         messages.success(request, "Registration successful." )
    #         return redirect("homepage")
    #     else:
    #         messages.error(request, form.errors)
    #         return redirect('register')
   

class Feedback(LoginRequiredMixin, TemplateView):
    template_name = 'user/feedback.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        doc_feed=FeedbackDoctor.objects.filter(user=self.request.user)
        hos_feed=FeedbackHospital.objects.filter(user=self.request.user)
        ngo_feed=FeedbackNgo.objects.filter(user=self.request.user)
        context={
            'feedbackdoclist':doc_feed,
            'feedbackhoslist':hos_feed,
            'feedbackngolist':ngo_feed,
            'formdoc':FeedbackDoctorForm,
            'formhos':FeedbackHospitalForm,
            'formngo':FeedbackNgoForm
        }
        return context

    def post(self, request):
        context={}
        if 'doctorfeedback' in request.POST:
            formdoc = FeedbackDoctorForm(request.POST)
            if formdoc.is_valid():
                form=formdoc.save(commit=False)
                form.user=request.user
                form.save()
                messages.success(request, "Thank you for your feedback." )
                return redirect("feedback")
            context['formdoc']=formdoc
        elif 'hospitalfeedback' in request.POST:
            formhos = FeedbackHospitalForm(request.POST)
            if formhos.is_valid():
                form=formhos.save(commit=False)
                form.user=request.user
                form.save()
                messages.success(request, "Thank you for your feedback." )
                return redirect("feedback")
            context['formhos']=formhos
        else:
            formngo = FeedbackNgoForm(request.POST)
            if formngo.is_valid():
                form=formngo.save(commit=False)
                form.user=request.user
                form.save()
                messages.success(request, "Thank you for your feedback." )
                return redirect("feedback")
            context['formngo']=formngo
        messages.success(request, "Please check form again. Invalid values." )
        return render(request, self.template_name, context=context)
   

class CremationView(LoginRequiredMixin, TemplateView):
    template_name = 'user/cremation.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context={
            'form':CremationForm,
            'cremation':Cremation.objects.filter(user=self.request.user)
        }
        return context

    def post(self, request):  
        context={} 
        form = CremationForm(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.user=request.user
            data.amount=100
            data.save()
            messages.success(request, "Within an hour all details will be send as SMS." )
            return redirect("cremation")
        messages.success(request, "Please check form again. Invalid values." )
        context['form']=CremationForm(request.POST)
        return render(request, self.template_name, context=context)
        
class FundraiseView(LoginRequiredMixin, TemplateView):
    template_name = 'user/fundraise.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context={
            'form':FundRaiseForm,
            'fundraise':FundRaise.objects.filter(user=self.request.user)
        }
        return context

    def post(self, request):  
        context={} 
        form = FundRaiseForm(request.POST, request.FILES)
        if form.is_valid():
            data=form.save(commit=False)
            data.user=request.user
            data.save()
            messages.success(request, "We hope you will soon able to raise funds." )
            return redirect("fundraise")
        messages.success(request, "Please check form again. Invalid values entered." )
        context['form']=form
        return render(request, self.template_name, context=context)



class ProfilePage(LoginRequiredMixin,UpdateView):
    form_class = CustomUserChangeForm
    template_name = 'user/profile.html'
    success_url= '/user/profile/'

    def get_object(self):
        return self.request.user