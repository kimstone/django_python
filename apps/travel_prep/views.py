from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

from . models import User

# Create your views here.

def index_view(request):
    context = {
        'page_title': "User Registration and Login",
        'page_meta_description': "SEO for User Registration & Login",
    }
<<<<<<< HEAD
    context['welcome_msg'] = "Welcome to the."
    return render(request, 'travel_prep/index.html', context)
=======
    return render(request, 'travel_prep/index.html')



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
>>>>>>> wip-registration-t03
