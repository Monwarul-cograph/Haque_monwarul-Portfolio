from django.shortcuts import render, redirect
from .models import * 
from .forms import *

# Create your views here.
def index(request):
    social = Social.objects.get()
    return render(request, 'index.html', {'social': social})

def about(request):
    about = About.objects.get()
    social = Social.objects.get()
    return render(request, 'about.html', {'about': about,'social': social})

def resume(request):
    resume = Resume.objects.get()
    social = Social.objects.get()
    return render(request, 'resume.html', {'resume': resume, 'social': social})

def portfolio(request):
    social = Social.objects.get()
    return render(request, 'portfolio.html', {'social':social})

def contact(request):
    social = Social.objects.get()
    # form = ContactForm(request.POST)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('index')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form, 'social':social})

