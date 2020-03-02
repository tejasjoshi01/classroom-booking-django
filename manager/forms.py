from .models import AvailableRooms , DateAndSlot 
from django.forms import ModelForm

class AddRoomForm(ModelForm):  
    class Meta:
        model  = AvailableRooms 
        fields = ['rooms_available']

class DateSlotForm(ModelForm):  
    class Meta:
        model  = DateAndSlot 
        fields = '__all__'

