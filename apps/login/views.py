from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
def index(request):
    return render(request, 'login/index.html')
def displayUser(request, userID):
    return render(request, 'login/users.html')

def register(request):

    register_response = User.objects.register(request.POST)
    if register_response['valid']:


        request.session['username'] = register_response['user'].username
        request.session['user_id'] = register_response['user'].id
        return redirect('projects:appoints')

    else:
        for error in register_response['errors']:
            messages.error(request, error)

        return redirect('/')


def login(request):
    
    login_response = User.objects.login(request.POST)
    if login_response['valid']:
        request.session['username'] = login_response['user'].username
        request.session['user_id'] = login_response['user'].id
        return redirect('projects:appoints')
    else:
        for error in login_response['errors']:
            messages.error(request, error)
        return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('logins:index')
