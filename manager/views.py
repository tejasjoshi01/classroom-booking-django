#imports from django utils
from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required

#import datetime library
from datetime import date, timedelta

#import models and forms
from .models import AvailableRooms , DateAndSlot , Room
from .forms import AddRoomForm , DateSlotForm , DateRangeForm
from customer.models import RoomBooking


# view for manager dashboard.
@staff_member_required(login_url = '/login/')
def managerDashboard(request):
    return render(request , 'manager/managerDashboard.html')


#view for adding slot using DateSlotForm.
@staff_member_required(login_url = '/login/')
def addSlot(request):

    if request.POST: 
        form_ds = DateSlotForm(request.POST)
        if form_ds.is_valid():
            form_ds.save()
            messages.success(request, 'Slot Added Successfully!')      
            return managerDashboard(request)

    form_ds = DateSlotForm()
    content = { 'form' : form_ds }
    return render(request , 'manager/addSlot.html' , content)


# View for displaying all slots. 
@staff_member_required(login_url = '/login/')
def addRooms(request , slot_id = None):
    slot_list_booked = DateAndSlot.objects.filter(rooms_added = True).order_by('booking_date') # query for slot for which rooms are alloted
    slot_list_unbooked = DateAndSlot.objects.filter(rooms_added = False).order_by('booking_date') # query for slot for which rooms are not alloted


    content = { 
        'slot_list_booked': slot_list_booked ,
        'slot_list_unbooked' : slot_list_unbooked
    }
    return render(request , 'manager/addRoom.html' , content)



#View for adding room
@staff_member_required(login_url = '/login/')
def addRooms_2(request , slot_id = None):
    selected_slot_obj = DateAndSlot.objects.get(pk = slot_id) # get slot for a particular id .
    
    if request.POST: 
        # generate room objects for a particular slot
        n = AvailableRooms(booking_date_slot = selected_slot_obj )
        get_room_count_form = AddRoomForm(request.POST , instance = n)

        if get_room_count_form.is_valid():
            get_room_count_form.save()
            n.save()


            for room_no in range(1 ,n.rooms_available+1):
                r = Room(chosen_date_slot = selected_slot_obj , room_number = room_no )
                r.save()

                
            ds = DateAndSlot.objects.get(pk = slot_id)
            ds.rooms_added = True
            ds.save()
            return managerDashboard(request)


    get_room_count_form = AddRoomForm()

    content = {
            'form': get_room_count_form ,
        }
    return render(request , 'manager/addRoom2.html' , content)



# get all the slot dates for which user has done bookings 
@staff_member_required(login_url = '/login/')
def getAllBookedDates(request):
    booking_dates = DateAndSlot.objects.filter(rooms_added = True).order_by('booking_date')
    content = {
        'booking_dates' : booking_dates
    }
    return render(request , 'manager/getAllBookedDates.html' ,content )


# get all the bookings for selected slot
@staff_member_required(login_url = '/login/')
def getSlotBookingDetail(request , slot_id):
    bookings_per_date = RoomBooking.objects.filter(booking_date_slot = slot_id).order_by('booked_room_number')
    content = {
            'bookings_per_date' : bookings_per_date 
    }
    return render(request , 'manager/getSlotBookingDetail.html' ,content )

# get details of User Booking .
def userBookingDetail(request , booking_id):
    user_booking_detail = get_object_or_404( RoomBooking , pk = booking_id)
    if request.method == 'POST':
        user_booking_detail.booked_room_number.is_booked = False 
        user_booking_detail.booked_room_number.save()
        user_booking_detail.delete()
        messages.success(request, 'Booking Cancelled Successfully!!')
        return redirect(reverse('getAllBookedDates' ))

    content = {
        'user_booking' : user_booking_detail 
    }
    return render(request , 'manager/userBookingDetail.html' , content)




























