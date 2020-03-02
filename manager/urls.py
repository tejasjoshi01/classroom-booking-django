from . import views 
from django.urls import path 


urlpatterns = [
    path('managerdashboard' , views.managerDashboard , name = 'managerDashboard' ) ,
    path('addroom' , views.addRooms , name = 'addRooms') , 
    path('addroom/<int:slot_id>' , views.addRooms_2 , name = 'addRooms') , 
    path('addslot' , views.addSlot , name = 'addSlot' )
]
