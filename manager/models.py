#Django utils import
from django.db import models
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandError

#import datetime libraray
from datetime import datetime, timedelta
import datetime

#self written models 




SLOT_CHOICES = (
    ('Slot 1' , 'S1') , 
    ('Slot 2' , 'S2') ,
)
class DateAndSlot(models.Model):
    booking_date = models.DateField(blank = False )
    booking_slot = models.TextField(choices = SLOT_CHOICES, blank = False)
    rooms_added = models.BooleanField(default = False)
    
    # DateAndSlot model methods for validation
    class Meta :
        unique_together = ('booking_date', 'booking_slot')

    def save(self, *args, **kwargs ):
        if self.booking_date < datetime.date.today():
            raise ValidationError("date must be in future")
        super(DateAndSlot, self).save(*args, **kwargs)
    
    def handle(self, *args, **options):
        DateAndSlot.objects.filter(booking_date - timedelta(days=1)).delete()
        self.stdout.write('Deleted objects older than 10 days')

    def __str__(self):
        return ("Date : {0} \n Slot: {1}" .format(self.booking_date , self.booking_slot ))




# Model for declaring rooms for particular time slot
class AvailableRooms(models.Model):
    booking_date_slot = models.OneToOneField(DateAndSlot , on_delete=models.CASCADE , blank=False , unique = True)
    rooms_available = models.IntegerField(null = True) 

    def __str__(self):
        return ("Booking Date : {0} \n Booking Slot: {1} \n Available Rooms: {2} " .format(self.booking_date_slot.booking_date , self.booking_date_slot.booking_slot , self.rooms_available ))




#Model for generating rooms object for particular slot.
class Room(models.Model):
    chosen_date_slot = models.ForeignKey('DateAndSlot' , on_delete = models.CASCADE ) 
    room_number      = models.IntegerField()
    is_booked        = models.BooleanField(default = False)


    def __str__(self):
        return ("Room No : {0} => {1}".format(self.room_number , self.chosen_date_slot)) 

