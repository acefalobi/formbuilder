from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .forms import *
from .models import *

from datetime import datetime, timedelta

# Create your views here.
def landing_page(request):
    return HttpResponseRedirect('/login')
    # return HttpResponse("Hello World. You're at the FormBuilder index")

def login_redirection_page(request):
    return HttpResponseRedirect('/login')

def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success')
    else:
        form = RegistrationForm()

    variables = {
        'form' : form
    }
    return render(request, "registration/register.html", variables)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
