from django.urls import path
from . import views


app_name='attend'
urlpatterns = [
    path("add_user",views.Add_user,name='Add_user'),
    path("checkin",views.Checkin,name='Checkin'),
    path("checkout",views.Checkout,name='Checkout'),
    path("report",views.Report,name='report'),
]
