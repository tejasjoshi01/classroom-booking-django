#Importing django utils 
from django.shortcuts import render , redirect , get_object_or_404
from django.contrib import messages
from django.http import HttpResponse , Http404 
from django.urls import reverse
from django.contrib.auth.decorators import login_required

#Import Model and Forms
from .forms import RoomBookingForm
from manager.models import DateAndSlot , Room , AvailableRooms
from .models import RoomBooking 

#import system datetime
import datetime

#Customer Dashboard 
@login_required(login_url='/login/')
def customerDashboard(request): 
    
    room_list = Room.objects.filter(is_booked = False) # all unbooked room objects
    
    date_slot_list = []
    for room in room_list:
        if room.chosen_date_slot not in date_slot_list:
            date_slot_list.append(room.chosen_date_slot)

    all_date_slot_list = DateAndSlot.objects.all().order_by('booking_date')

    full_slots = list(set(all_date_slot_list) - set(date_slot_list))

    # getting full slots and available slots

    content = {
            'full_slots'     : full_slots ,
            'date_slot_list' : date_slot_list ,
        }
    return render(request,"customer/customerDashboard.html",content) 


# display the rooms available for particular slot
@login_required(login_url='/login/')
def displayRooms(request, slot_id):

    selected_slot_obj = DateAndSlot.objects.get(pk = slot_id)
    room_list_for_slot = Room.objects.filter(chosen_date_slot = selected_slot_obj , is_booked = False) # Display unbooked rooms for the selected slot

    content = {
        'room_list_for_slot': room_list_for_slot
    }
    return render(request , "customer/displayRooms.html" , content)


# For displaying all the user bookings 
@login_required(login_url='/login/')
def getUserBookings(request):

    user_booking_list = RoomBooking.objects.filter(bookee_username = request.user) # User Bookings
    current_date = datetime.date.today()


    content = {
            'user_booking_list' : user_booking_list ,
            'today'             : current_date ,
        }
    return render(request , 'customer/userBookings.html' , content)



# Room booking view.
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
            messages.success(request, 'Booking Done Successfully!!')
            return redirect(reverse('userRoomBooking'))
            



    # Handle GET request
    form = RoomBookingForm()
    room_number = Room.objects.get(pk = room_id).room_number
    content = {
        'room_number':room_number ,
        'form':form
    }
    return render(request,"customer/customerRoomBooking.html" , content)



# Get the details of user bookings .
def deatiledUserBooking(request , booking_id):
    user_booking_detail = get_object_or_404( RoomBooking , pk = booking_id)
    
    if request.method == 'POST':
        user_booking_detail.booked_room_number.is_booked = False 
        user_booking_detail.booked_room_number.save()
        user_booking_detail.delete()
        messages.success(request, 'Booking Cancelled Successfully!!')
        return redirect(reverse('userRoomBooking'))


    content = {
        'booking' : user_booking_detail ,
    }
    return render(request , 'customer/detailedUserBooking.html' , content)