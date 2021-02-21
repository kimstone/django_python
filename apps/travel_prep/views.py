from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

from . models import Trip, User

# Create your views here.

def add_trips_view(request):
    context = {
        'page_title': "Add Trip",
    }

    if request.method == "POST":
        errors = Trip.objects.validate_trip_form(request.POST)

        if len(errors) > 0:

            for key, value in errors.items():
                messages.error(request, value, extra_tags='trip-form')

            return redirect('/')
        else:
            user = User.objects.get(id=request.session['user_id'])
            new_trip = Trip.objects.create_new_trip(request.POST, user)
            return redirect('travel_prep/trips')
    return render(request, 'travel_prep/add-trip.html', context)



def authenticate_user_view(request):

    if request.method == "GET":
        return redirect('/')

    errors = User.objects.validate_login_form(request.POST)
    if len(errors) > 0:

        for key, value in errors.items():
            messages.error(request, value, extra_tags='login-form')

        return redirect('/')

    if not User.objects.authenticate_credentials(request.POST['email_address'], request.POST['password']):
        messages.error(request, 'You have entered an invalid email/password combo')
        return redirect('travel_prep/message')
    else:
        registered_user = User.objects.get(email=request.POST['email_address'])
        request.session['user_id'] = registered_user.id

        #messages.success(request, 'The User model listing ...', extra_tags='model-user')
        #context['users'] = User.objects.all()
        return redirect('travel_prep/trips')



def index_view(request):
    context = {
        'page_title': "User Registration and Login",
        'page_meta_description': "SEO for User Registration & Login",
    }
    context['welcome_msg'] = "Welcome to the."
    return render(request, 'travel_prep/index.html', context)



def cancel_trip_view(request, trip_id):

    user = User.objects.get(id=request.session['user_id'])
    this_trip = Trip.objects.get(id=trip_id)

    #DO NOT DELETE REMOVE
    user.trip_travelers.remove(this_trip)

    return redirect('travel_prep/trips')



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



def join_trip_view(request, trip_id):
    user = User.objects.get(id=request.session['user_id'])
    this_trip = Trip.objects.get(id=trip_id)
    user.trip_travelers.add(this_trip)
    return redirect('travel_prep/trips')



def logout_view(request):
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
    context['trips'] = Trip.objects.all()
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



def show_trips_view(request):
    context = {
        'page_title': "Show User Scheduled Trips",
    }
    user = User.objects.get(id=request.session['user_id'])
    user_planned_trips = user.trip_planner.all()
    user_joined_trips = user.trip_travelers.all()
    others_trips = Trip.objects.all().exclude(travelers=user).exclude(planner=user)
    context['user'] = user
    context['user_planned_trips'] = user_planned_trips
    context['user_joined_trips'] = user_joined_trips
    context['others_trips'] = others_trips
    return render(request, 'travel_prep/my-trips.html', context)

