from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request) :
    return render(request,'index.html')


def register(request) :
    if request.POST.get('reg-job-seeker') :
        return render(request,'register_jobseeker.html')
        
    if request.POST.get('reg-employer') :
        return render(request,'register_employer.html')    

    return render(request,'register.html')

def signin(request) :
    return render(request,'signin.html') 

def register_jobseeker(request) :
            form = UserCreationForm()
            
            if request.method == 'POST':
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
            context = {'form' : form}        
            return render(request, 'register_jobseeker.html',context)       