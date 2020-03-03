from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse , Http404



from .forms import RoomBookingForm
from manager.models import DateAndSlot , Room , AvailableRooms
from .models import RoomBooking 


  
def customerDashboard(request):  
    date_slot_list = DateAndSlot.objects.all().order_by('-booking_date')
    content = {
            'date_slot_list' : date_slot_list
        }
    return render(request,"customer/customerDashboard.html",content) 

def getUserBookings(request):
    user_booking_list = RoomBooking.objects.filter(bookee_username = request.user)
    content = {
            'user_booking_list' : user_booking_list
        }

    return render(request , 'customer/userBookings.html' , content)


def displayRooms(request, slot_id):
    selected_slot_obj = DateAndSlot.objects.get(pk = slot_id)
    room_list_for_slot = Room.objects.filter(chosen_date_slot = selected_slot_obj)

    content = {
        'room_list_for_slot': room_list_for_slot
    }
    return render(request , "customer/displayRooms.html" , content)

def customerRoomBooking(request, slot_id , room_id):
    rb = RoomBooking()
    rb.booked_room_number = Room.objects.get(pk = room_id)
    rb.bookee_username = request.user.username
    rb.booking_date_slot = DateAndSlot.objects.get(pk = slot_id )

    form = RoomBookingForm(request.POST , instance = rb)
    if form.is_valid():
        form.save()
        form = RoomBookingForm()
        # messages.info("Booking Done Check My Bookings for Details")

    context = {
        'form':form
    }
    return render(request,"customer/customerRoomBooking.html" , context)
