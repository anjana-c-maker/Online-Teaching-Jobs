from django.shortcuts import render

# Create your views here.
def index(request) :
    return render(request,'index.html')


def register(request) :
    if request.POST.get('reg-job-seeker') :
        return render(request,'register_jobseeker.html')

    return render(request,'register.html')