from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse , Http404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


from .forms import RoomBookingForm
from manager.models import DateAndSlot , Room , AvailableRooms
from .models import RoomBooking 


@login_required(login_url='/login/')
def customerDashboard(request): 
    room_list = Room.objects.filter(is_booked = False)
    
    date_slot_list = []
    for room in room_list:
        if room.chosen_date_slot not in date_slot_list:
            date_slot_list.append(room.chosen_date_slot)

    all_date_slot_list = DateAndSlot.objects.all()

    full_slots = list(set(all_date_slot_list) - set(date_slot_list))



    content = {
            'full_slots'     : full_slots ,
            'date_slot_list' : date_slot_list
        }
    return render(request,"customer/customerDashboard.html",content) 


@login_required(login_url='/login/')
def getUserBookings(request):
    user_booking_list = RoomBooking.objects.filter(bookee_username = request.user)
    content = {
            'user_booking_list' : user_booking_list
        }

    return render(request , 'customer/userBookings.html' , content)


@login_required(login_url='/login/')
def displayRooms(request, slot_id):
    selected_slot_obj = DateAndSlot.objects.get(pk = slot_id)
    room_list_for_slot = Room.objects.filter(chosen_date_slot = selected_slot_obj , is_booked = False)

    content = {
        'room_list_for_slot': room_list_for_slot
    }
    return render(request , "customer/displayRooms.html" , content)



@login_required(login_url='/login/')
def customerRoomBooking(request, slot_id , room_id):
    # Handle POST request
    if request.POST :
        rb = RoomBooking()
        rb.booked_room_number = Room.objects.get(pk = room_id)
        rb.bookee_username = request.user.username
        rb.booking_date_slot = DateAndSlot.objects.get(pk = slot_id )

        form = RoomBookingForm(request.POST , instance = rb)
        if form.is_valid():
            form.save()
            room = Room.objects.get(pk = room_id)
            room.is_booked = True
            room.save()



    # Handle GET request
    form = RoomBookingForm()
    room_number = Room.objects.get(pk = room_id).room_number
    context = {
        'room_number':room_number ,
        'form':form
    }
    return render(request,"customer/customerRoomBooking.html" , context)
