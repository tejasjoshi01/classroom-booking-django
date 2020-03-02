from django.urls import path 
from . import views


urlpatterns = [
    path('' , views.customerDashboard , name = "customerDashboard" ) ,
    path('<int:slot_id>/' , views.customerRoomBooking , name = 'customerRoomBooking') , 
    path('user-bookings/' , views.getUserBookings , name = 'userRoomBooking')
]
