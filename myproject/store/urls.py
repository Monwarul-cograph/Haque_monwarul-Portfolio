
from django.urls import path
from .views import *  

urlpatterns = [
   path('', index, name = 'index'),
   path('about/', about, name = 'about'),
   path('resume/', resume, name = 'resume'),
   path('contact/', contact, name = 'contact'),
   path('portfolio/', portfolio, name = 'portfolio')
]

