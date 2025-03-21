from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',login,name="login"),
    path('dashboard.html',dashboard, name = "Dashboard"),
    path('login/',staff_login,name="Login View"),
    path('logout/',staff_logout,name="Logout View"),
    path('createstaff/',create_a_new_staff,name="Create a new Staff"),
    path('details/',get_details_of_the_staff,name="Details of the staff")
]