from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name="travel_prep/index"),
    path('add/', views.add_trips_view, name="travel_prep/add-trip"),
    path('cancel/<int:trip_id>', views.cancel_trip_view, name="travel_prep/cancel"),
    path('delete/<int:trip_id>', views.delete_trip_view, name="travel_prep/delete"),
    path('destination/<int:trip_id>', views.show_destination_view, name="travel_prep/destination"),
    path('login/', views.authenticate_user_view, name="travel_prep/login"),
    path('db-data/', views.show_db_objects_view, name="travel_prep/db_object_listing"),
    path('db-data-all/', views.show_db_objects_all_view, name="travel_prep/db_object_all_listing"),
    path('join/<int:trip_id>', views.join_trip_view, name="travel_prep/join"),
    path('logout/', views.logout_view, name="travel_prep/logout"),
    path('my-trips/', views.show_trips_view, name="travel_prep/trips"),
    path('message/', views.show_information_view, name="travel_prep/message"),
    path('register/', views.create_user_view, name="travel_prep/register"),
]