from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name="travel_prep/index"),
    path('login/', views.authenticate_user_view, name="travel_prep/login"),
    path('db-data/', views.show_db_objects_view, name="travel_prep/db_object_listing"),
    path('db-data-all/', views.show_db_objects_all_view, name="travel_prep/db_object_all_listing"),
    path('logout/', views.logout, name="travel_prep/logout"),
    path('message/', views.show_information_view, name="travel_prep/message"),
    path('register/', views.create_user_view, name="travel_prep/register"),
]