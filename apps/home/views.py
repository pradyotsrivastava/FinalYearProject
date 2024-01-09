import json
from urllib import request
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib import messages
import datetime
from apps.feedback.models import *
from django.db.models import Avg, Q
from apps.seminar.forms import SeminarAttendeesForms
from apps.seminar.models import Seminar
from .models import State, City, Specialization


class Homepage(TemplateView):
    template_name = 'home/index.html'

    def get(self, request):
        context={}
        top_doc=FeedbackDoctor.objects.values('doctor').annotate(rating=Avg('rating')).order_by('-rating').first()
        doc=Doctors.objects.get(id=top_doc['doctor'])
        top_hos=FeedbackHospital.objects.values('hospital').annotate(rating=Avg('rating')).order_by('-rating').first()
        hos=Hospital.objects.get(id=top_hos['hospital'])
        top_ngo=FeedbackNgo.objects.values('ngo').annotate(rating=Avg('rating')).order_by('-rating').first()
        ngo=Ngo.objects.get(id=top_ngo['ngo'])
        
        context={
            'top_doc':doc,
            'rating_doc':top_doc['rating'],
            'top_hos':hos,
            'rating_hos':top_hos['rating'],
            'top_ngo':ngo,
            'rating_ngo':top_ngo['rating'],
        }
        return render(request, self.template_name, context)


class SearchPage(TemplateView):
    template_name = 'home/searchpage.html'

    def get(self, request):
        context={}
        search_for = request.GET.get('search_for')
        searched = request.GET.get('search','')
        state = request.GET.get('state', '')
        city = request.GET.get('city', '')
        category = request.GET.get('category','')
        poison = request.GET.get('poison')
        beds = request.GET.get('beds')
        oxygen = request.GET.get('oxygen')
        context={
                'search': searched,
                'search_for':search_for
        }
        if search_for is not None:
            if search_for=="doctors":
                print(searched, city)
                print(state, category)
                all_doctors = Doctors.objects.filter(Q(name__contains=searched) & Q(hospital__city__name__contains=city) & Q(hospital__city__state__name__contains=state) & Q(specialization__name__contains=category)).order_by('name')
                context['doctors']=all_doctors
            elif search_for=="hospitals":
                all_hospitals = Hospital.objects.filter(Q(name__contains=searched) & Q(city__name__contains=city) & Q(city__state__name__contains=state)).order_by('name')
                if bool(poison):
                    all_hospitals=all_hospitals.filter(hospitalinfo__poison_cell=bool(poison))
                if bool(oxygen):
                    all_hospitals=all_hospitals.filter(hospitalinfo__oxygen=bool(oxygen))
                context['hospitals'] = all_hospitals 
            elif search_for=="ngo":
                all_ngos = Ngo.objects.filter(Q(name__contains=searched) & Q(city__name__contains=city)).order_by('name')
                context['ngos']=all_ngos


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
        return render(request, self.template_name, context)


class SeminarPage(TemplateView):
    template_name = 'home/seminar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        upSeminars=Seminar.objects.filter(date__gt=datetime.date.today())
        context['upSeminars']=upSeminars
        pastSeminars=Seminar.objects.filter(date__lt=datetime.date.today())
        context['pastSeminars']=pastSeminars
        context['form']=SeminarAttendeesForms
        return context
    

    def post(self, request):
        context={} 
        form = SeminarAttendeesForms(request.POST)
        val=request.POST.get('buttonId', None)
        obj=Seminar.objects.get(id=val)
        if form.is_valid():
            data=form.save(commit=False)
            data.seminar=obj
            data.save()
            messages.success(request, "Register successfully for the seminar." )
            return redirect("seminar")
        context['form']=form
        return render(request, self.template_name, context=context)
