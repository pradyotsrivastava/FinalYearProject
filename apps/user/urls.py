from django.urls import path
from .views import *
urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('profile/', ProfilePage.as_view(), name='profile'),
    path('feedback/', Feedback.as_view(), name='feedback'),
    path('fundraise/', FundraiseView.as_view(), name='fundraise'),
    path('cremation/', CremationView.as_view(), name='cremation'),

]
