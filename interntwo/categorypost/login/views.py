from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import  SignUpForm,ProfileForm
from .models import StudentProfile
from django.contrib.auth.models import User

#from django.contrib.auth.forms import UserCreationForm

#this method is for showing home page and showing total number of users registered in this site

# def home(request):
#     """
#     total users registered
#     """
#     all_user = User.objects.all()
#     user_number = len(all_user)
#     context = {'user_number': user_number}
#     return render(request, 'home.html',context)



#this is for sign up


def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # create user
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('/login')
    form = SignUpForm()
    return render(request, 'signup.html',{'signup_form':form})

#this is for login

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'postcategory.html')
        else:
            return HttpResponse("Username or password incorrect")
    return render(request, 'login.html')


#this is for logout


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')



def apply(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return render(request, 'showprofile.html')
    context={
        "form":form
    }
    return render(request, 'profile.html',context)

def showprofile (request, name):
    show=StudentProfile.objects.get(user__username=name)
    contex ={'show': show}
    return render(request, 'showprofile.html',contex)