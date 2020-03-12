from django.db import models
from manager.models import AvailableRooms , DateAndSlot , Room


class RoomBooking(models.Model):
    booking_date_slot = models.ForeignKey(DateAndSlot , on_delete=models.CASCADE , blank=False)
    booked_room_number = models.OneToOneField(Room , unique = True , on_delete = models.CASCADE , blank = False)
    bookee_username = models.CharField(max_length = 50 , blank = False , default = 'Admin')
    
    #field to be taken as input
    customer_name = models.CharField(max_length = 60 , blank=False)
    customer_email = models.EmailField(unique = True, max_length=254)
    customer_contact = models.CharField(unique = True , max_length = 12)
    booking_purpose = models.CharField(max_length = 254 , blank = True)

    def __str__(self):
        return self.customer_name 
