from django import forms 
from manager.models import DateAndSlot 
from .models import CustomerBooking 


class CustomerBookingForm(forms.ModelForm):
    class Meta:  
        model = CustomerBooking  
        fields = ('customer_name' , 'customer_email' , 'customer_contact' , 'booking_purpose' , 'booked_room_number')

