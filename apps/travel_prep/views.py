from django.shortcuts import render, redirect
from django.contrib import messages

from . models import *

# Create your views here.

def index_view(request):
    context = {
        'page_title': "Page Title",
        'page_meta_description': "Page Meta Description",
    }
    context['welcome_msg'] = "Welcome to the Sample Page."
    return render(request, 'travel_prep/index.html', context)
