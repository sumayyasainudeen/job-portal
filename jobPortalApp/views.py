from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User,auth
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request, anchor=None):
     return render(request,'index.html')

def software(request):
     return render(request,'software.html')

def js_signin_page(request):
    return render(request,'js_signin.html')

def js_signup_page(request):
    return render(request,'js_signup.html')

def jobseeker_signup(request):
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        uname = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(first_name=fname,last_name=lname,email=email,username=uname,password=password)
        user.save()
        return redirect('js_signin_page')
    else:
        return redirect('js_signup_page')
    
def jobseeker_signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            auth.login(request, user)
            return redirect('index')
        else:
            return redirect('js_signin_page')
    return redirect('js_signin_page')

def signout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('index')
    
@login_required(login_url='js_signin_page')
def resume_upload_page(request):
    return render(request,'uploadresume.html')

def myjobs(request):
    return render(request,'myjobs.html')

def message(request):
    return render(request,'message.html')

def notifications(request):
    return render(request,'notifications.html')
# -----------------------------------------------------

def em_signin_page(request):
    return render(request,'em_signin.html')

def em_signup_page(request):
    return render(request,'em_signup.html')

def employer_signup(request):
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        uname = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(first_name=fname,last_name=lname,email=email,username=uname,password=password)
        user.save()
        return redirect('em_signin_page')
    else:
        return redirect('em_signup_page')
    
def employer_signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            auth.login(request, user)
            return redirect('emp_home')
        else:
            return redirect('em_signin_page')
    return redirect('em_signin_page')

def emp_home(request):
    return render(request,'emp_home.html')

@login_required(login_url='em_signin_page')
def post_job_page(request):
    return render(request,'postjob.html')

@login_required(login_url='em_signin_page')
def create_company(request):
     return render(request,'createcompany.html')

def postedjobs(request):
    return render(request,'postedjobs.html')

def editjob(request):
    return render(request,'editjob.html')


