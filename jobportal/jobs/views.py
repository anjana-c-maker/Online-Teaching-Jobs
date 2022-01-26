from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm 
from jobs.forms import CustomForm
# Create your views here.

def index(request) :
    return render(request,'index.html')


def register(request) :  

    return render(request,'register.html')


def register_jobseeker(request) :
            form = CustomForm()
            if request.method == 'POST':
                form = CustomForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('accounts:login')
            context = {
                "form":form
            } 
            return render(request, 'register_jobseeker.html', context)  


def register_employer(request) :
            form = CustomForm()
            if request.method == 'POST':
                form = CustomForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('accounts:login')
            context = {
                "form":form
            } 
            return render(request, 'register_employer.html', context)  


