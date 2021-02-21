from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name="travel_prep/index"),
    path('authenticate/', views.authenticate_user_view, name="travel_prep/authenticate"),
    path('logout/', views.logout, name="travel_prep/logout"),
    path('message/', views.show_information_view, name="travel_prep/information"),
    path('register/', views.create_user_view, name="travel_prep/register"),
]