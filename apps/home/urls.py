from django.urls import path

from .views import Homepage, SearchPage, SeminarPage

urlpatterns = [
   path('', Homepage.as_view(),name='homepage'),
   path('search/', SearchPage.as_view(),name='search'),
   
   path('doctor/<uuid:id>/', Homepage.as_view(),name='doctor-detail'),
   path('hospital/<uuid:id>/', SearchPage.as_view(),name='hospital-detail'),
   path('ngo/<uuid:id>/', SearchPage.as_view(),name='ngo-detail'),
   path('seminar/', SeminarPage.as_view(), name='seminar')

   # path('error/', Accessdenied.as_view(), name='access-denied'),
]