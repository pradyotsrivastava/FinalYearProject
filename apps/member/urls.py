from django.urls import path

from  .views import UserLoginPage, UserRegisterPage, HospitalLoginPage, HospitalRegisterPage, logoutpage

urlpatterns = [
   path('login/', UserLoginPage.as_view(), name='login'),
   path('register/', UserRegisterPage.as_view(), name='register'),
   
   path('hospital/login/', HospitalLoginPage.as_view(), name='hospital-login'),
   path('hospital/register/', HospitalRegisterPage.as_view(), name='hospital-register'),

   path('logout/', logoutpage, name='logout'),
]