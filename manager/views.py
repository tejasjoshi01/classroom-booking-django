from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages


from .models import AvailableRooms , DateAndSlot , Room
from .forms import AddRoomForm , DateSlotForm 



def managerDashboard(request):
    return render(request , 'manager/managerDashboard.html')


def addSlot(request):
    form_ds = DateSlotForm()
    if request.method == 'POST':
        if form_ds.is_valid():
            form_ds.save()
        return managerDashboard(request)

    else:
        context = { 'form' : form_ds }
        return render(request , 'manager/addSlot.html' , context)



def addRooms(request , slot_id = None):
    slot_list = DateAndSlot.objects.all()
    context = { 
        'slot_list' : slot_list
    }
    return render(request , 'manager/addRoom.html' , context)


def addRooms_2(request , slot_id = None):
    selected_slot_obj = DateAndSlot.objects.get(pk = slot_id)
    n = AvailableRooms(booking_date_slot = selected_slot_obj )
    get_room_count_form = AddRoomForm(request.POST , instance = n)

    if get_room_count_form.is_valid():
        get_room_count_form.save()
        n.save()
        for room_no in range(1 ,n.rooms_available+1):
            r = Room(chosen_date_slot = selected_slot_obj , room_number = room_no )
            r.save()
        messages.info(request, 'Rooms Saved Successfully')
        get_room_count_form = AddRoomForm()


    context = {
            'form': get_room_count_form ,
        }
    return render(request , 'manager/addRoom2.html' , context)



