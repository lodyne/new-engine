from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from .forms import RegistrationForm

# Create your views here.
# def logout(request):
#     messages.success(request,"You have successfull logout")
#     return logout_then_login(request,'core/login.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegistrationForm()
    
    context = {
        'form': form
    }

    return render(request,'users/signup.html',context)

