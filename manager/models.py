from django.db import models


SLOT_CHOICES = (
    ('Slot 1' , 'S1') , 
    ('Slot 2' , 'S2') ,
)

class DateAndSlot(models.Model):
    booking_date = models.DateField(blank = False )
    booking_slot = models.TextField(choices = SLOT_CHOICES, blank = False)

    def __str__(self):
        return ("Date : {0} \n Slot: {1}" .format(self.booking_date , self.booking_slot ))

class AvailableRooms(models.Model):
    booking_date_slot = models.OneToOneField(DateAndSlot , on_delete=models.CASCADE , blank=False , unique = True)
    rooms_available = models.IntegerField(null = True) 

    def __str__(self):
        return ("Booking Date : {0} \n Booking Slot: {1} \n Available Rooms: {2} " .format(self.booking_date_slot.booking_date , self.booking_date_slot.booking_slot , self.rooms_available ))


class Room(models.Model):
    chosen_date_slot = models.ForeignKey('DateAndSlot' , on_delete = models.CASCADE ) 
    room_number      = models.IntegerField()

    def __str__(self):
        return ("Room No : {0} => {1}".format(self.room_number , self.chosen_date_slot)) 

