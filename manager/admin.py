from django.contrib import admin
from .models import DateAndSlot , AvailableRooms , Room
# Register your models here.



allModels = [

    DateAndSlot ,
    AvailableRooms ,
    Room

]


admin.site.register(allModels)
