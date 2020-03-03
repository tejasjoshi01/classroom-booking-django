from django.urls import path 
from . import views


urlpatterns = [
    path('' , views.customerDashboard , name = "customerDashboard" ) ,
    path('<int:slot_id>/' , views.displayRooms , name = 'displayRooms') , 
    path('<int:slot_id>/<int:room_id>/' , views.customerRoomBooking , name = 'customerRoomBooking') , 
    path('user-bookings/' , views.getUserBookings , name = 'userRoomBooking')
]
