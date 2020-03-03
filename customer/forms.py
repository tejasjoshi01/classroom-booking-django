from django import forms 
from manager.models import DateAndSlot 
from .models import RoomBooking 


class RoomBookingForm(forms.ModelForm):
    class Meta:  
        model = RoomBooking  
        fields = ('customer_name' , 'customer_email' , 'customer_contact' , 'booking_purpose')

