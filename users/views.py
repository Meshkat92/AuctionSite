from django.shortcuts import render
from users.forms import RegistrationForm,LoginForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(request):
    """Auction site home page"""
    return render(request, 'users/home.html')

def login(request):
    """Login an existing user"""
    if request.method != 'POST':
        # Display blank login form
        form = LoginForm()
    else:
        form = LoginForm(data=request.POST)
    if form.is_valid():
        return HttpResponseRedirect(reverse('users:home'))
    
    context = {'form': form}
    return render(request, 'users/login.html', context)
    

def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # Display blank registration form
        form = RegistrationForm()
    else:
        # Process completed form
        form =  RegistrationForm(data=request.POST)

    if form.is_valid():
        new_user = form.save()
        # Log the user in and redirect to home page
        authenticated_user = authenticate(username=new_user.username,email=new_user.email)
        login(request,authenticated_user)
        return HttpResponseRedirect(reverse('users:login'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
        
