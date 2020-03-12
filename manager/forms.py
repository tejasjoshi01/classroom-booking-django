from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms

import datetime
from .models import AvailableRooms , DateAndSlot 






#Form for taking inputs of DateSlotModel
class DateInput(forms.DateInput):
    input_type = 'date'


#Forms for adding a particular slots
class DateSlotForm(forms.ModelForm):
    class Meta:
        model = DateAndSlot
        fields = ('booking_date', 'booking_slot')
        widgets = {
            'booking_date': DateInput()

        }


#Form for taking inputs of AvailableRooms
class AddRoomForm(ModelForm):  
    class Meta:
        model  = AvailableRooms 
        fields = ['rooms_available']

#Form taking inputs in form of Date
class DateRangeForm(forms.Form):
    start_date = forms.DateField(label = 'From Date', required = True , widget = DateInput() )
    end_date   = forms.DateField(label = 'End Date', required = True , widget = DateInput() )



