from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm 
# Create your views here.
def index(request) :
    return render(request,'index.html')


def register(request) :  

    return render(request,'register.html')


def register_jobseeker(request) :
            form = UserCreationForm()
            if request.method == 'POST':
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('signin')
            context = {
                "form":form
            } 
            return render(request, 'register_jobseeker.html', context)  

def signin(request) :
    return render(request,'signin.html') 

def register_employer(request) :  

    return render(request,'register_employer.html')

