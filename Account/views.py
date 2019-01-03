from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.


def home(request):
    context = {}
    return render(request, 'home.html', context)


def signupform(request):
    context={}
    return render(request, 'signupform.html', context)


def signup(request):
    if request.POST['password'] == request.POST['cpassword']:
        try:
            user = User.objects.get(username= request.POST['uname'])
            return render(request, 'signupform.html', {'error': 'Username is already taken. Try something new'})
        except:
            user = User.objects.create_user(username=request.POST['uname'], password=request.POST['password'])
            auth.login(request, user)
            return redirect('loginform')
    else:
        return render(request, 'signupform.html', {'error':'Password doesn\'t match'})


def loginform(request):
    context = {}
    return render(request, 'loginform.html', context)


def login(request):
    user = auth.authenticate(username=request.POST['uname'], password=request.POST['password'])
    if user is not None:
        auth.login(request, user)
        #return render(request, 'loginsuccess.html', {'success': 'Login is successful'})
        return redirect('getall')
    else:
        return render(request, 'loginform.html', {'failure': 'Username or password doesn\'t match' })


def signout(request):
    auth.logout(request)
    return render(request, 'home.html', {'message':'You are signed out'})