from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

from . models import User

# Create your views here.

def authenticate_user_view(request):

    if request.method == "GET":
        return redirect('/')

    if not User.objects.authenticate_credentials(request.POST['email_add'], request.POST['password']):
        messages.error(request, 'You have entered an invalid email/password combo')
        return redirect('access_control/login_form')
    else:
        registered_user = User.objects.get(email=request.POST['email_add'])
        request.session['user_id'] = registered_user.id
        request.session['success_msg'] = "You have successfully logged in!"

        if registered_user.user_level != 9:
            return redirect('access_control/user_directory')
        else:
            return redirect('access_control/dashboard-admin')



def index_view(request):
    context = {
        'page_title': "User Registration and Login",
        'page_meta_description': "SEO for User Registration & Login",
    }
    context['welcome_msg'] = "Welcome to the."
    return render(request, 'travel_prep/index.html', context)



def create_user_view(request):

    if request.method == "GET":
        return redirect('/')

    #errors = {}
    errors = User.objects.validate_registration_form(request.POST)

    if len(errors) > 0:

        for key, value in errors.items():
            messages.error(request, value, extra_tags='registration-form')

        return redirect('/')
    else:
        new_user = User.objects.create_new_user(request.POST)
        request.session['user_id'] = new_user.id
        messages.success(request, "You have successfully registered!")
        return redirect('travel_prep/information')



def logout(request):
    request.session.clear()
    return redirect('/')



def show_information_view(request):
    context = {
        'page_title': "Communication with User",
        'page_meta_description': "SEO for Communication with User",
    }
    obj = User.objects.get(id=request.session['user_id'])
    context['object'] = obj
    return render(request, 'travel_prep/message.html', context)

