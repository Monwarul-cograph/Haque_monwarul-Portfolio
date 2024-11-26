from django.shortcuts import render
from .models import * 

# Create your views here.
def index(request):
    social = Social.objects.get()
    return render(request, 'index.html', {'social': social})

def about(request):
    about = About.objects.get()
    return render(request, 'about.html', {'about': about})

def resume(request):
    return render(request, 'resume.html')

def contact(request):
    if request.method == 'POST'
    return render(request, 'contact.html')