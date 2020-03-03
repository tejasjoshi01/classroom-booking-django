from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms

import datetime
from .models import AvailableRooms , DateAndSlot 



#Form for taking inputs of DateSlotModel

class DateInput(forms.DateInput):
    input_type = 'date'

class DateSlotForm(forms.ModelForm):
    class Meta:
        model = DateAndSlot
        fields = ('booking_date', 'booking_slot')
        widgets = {
            'booking_date': DateInput()
        }
 





class Projectform(forms.ModelForm):
    def __init__(user_project, request, *args, **kwargs):
        self.user_project = user_project
        self.request = request
        super().__init__(*args, **kwargs)




















#Form for taking inputs of AvailableRooms
class AddRoomForm(ModelForm):  
    class Meta:
        model  = AvailableRooms 
        fields = ['rooms_available']


