from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

from . models import User

# Create your views here.

def authenticate_user_view(request):

    if request.method == "GET":
        return redirect('/')

    if not User.objects.authenticate_credentials(request.POST['email_address'], request.POST['password']):
        messages.error(request, 'You have entered an invalid email/password combo')
        return redirect('travel_prep/message')
    else:
        registered_user = User.objects.get(email=request.POST['email_address'])
        request.session['user_id'] = registered_user.id

        messages.success(request, 'The User model listing ...', extra_tags='model-user')
        #context['users'] = User.objects.all()
        return redirect('travel_prep/db_object_listing')



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
        return redirect('travel_prep/message')



def logout(request):
    request.session.clear()
    return redirect('/')



def show_db_objects_view(request):
    context = {
        'page_title': "Display DB Objects to Developer",
    }
    #obj = User.objects.get(id=request.session['user_id'])
    #context['object'] = obj
    return render(request, 'travel_prep/db_objects.html', context)



def show_db_objects_all_view(request):
    context = {
        'page_title': "Show All DB Objects",
    }
    context['users'] = User.objects.all()
    return render(request, 'travel_prep/db_objects_all.html', context)



def show_information_view(request):
    context = {
        'page_title': "Communication with User",
        'page_meta_description': "SEO for Communication with User",
    }

    if 'user_id' not in request.session:
        greeting = 'Please Login'
    else:
        obj = User.objects.get(id=request.session['user_id'])
        greeting = f"Hello, {obj.first_name}"

    context['greeting'] = greeting
    return render(request, 'travel_prep/message.html', context)

