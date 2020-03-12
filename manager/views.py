#imports from django utils
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
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
            return managerDashboard(request)

    form_ds = DateSlotForm()
    context = { 'form' : form_ds }
    return render(request , 'manager/addSlot.html' , context)


# View for displaying all slots. 
@staff_member_required(login_url = '/login/')
def addRooms(request , slot_id = None):
    slot_list_booked = DateAndSlot.objects.filter(rooms_added = True).order_by('booking_date')
    slot_list_unbooked = DateAndSlot.objects.filter(rooms_added = False).order_by('booking_date')


    context = { 
        'slot_list_booked': slot_list_booked ,
        'slot_list_unbooked' : slot_list_unbooked
    }
    return render(request , 'manager/addRoom.html' , context)



#View for adding room
@staff_member_required(login_url = '/login/')
def addRooms_2(request , slot_id = None):
    selected_slot_obj = DateAndSlot.objects.get(pk = slot_id)
    
    if request.POST: 
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
    context = {
            'form': get_room_count_form ,
        }
    return render(request , 'manager/addRoom2.html' , context)



@staff_member_required(login_url = '/login/')
def getAllBookedDates(request):
    booking_dates = DateAndSlot.objects.filter(rooms_added = True).order_by('booking_date')
    content = {
        'booking_dates' : booking_dates
    }
    return render(request , 'manager/getAllBookedDates.html' ,content )



@staff_member_required(login_url = '/login/')
def getSlotBookingDetail(request , slot_id):
    bookings_per_date = RoomBooking.objects.filter(booking_date_slot = slot_id).order_by('booked_room_number')
    content = {
            'bookings_per_date' : bookings_per_date 
    }
    return render(request , 'manager/getSlotBookingDetail.html' ,content )

def userBookingDetail(request , booking_id):

    user_booking = RoomBooking.objects.get(pk = booking_id)

    content = {
        'user_booking' : user_booking 
    }
    return render(request , 'manager/userBookingDetail.html' , content)





























@staff_member_required(login_url = '/login/')
def getDatesRange(request):
    pass
    '''
    form = DateRangeForm()

    if request.method == 'POST':
        if form.is_valid():

            dates = request.POST.copy()

            print("valid 1")
            date_range = []

            start_date = dates.cleaned_data['start_date'] ,
            print(start_date)
            end_date = dates.cleaned_data['end_date']
            print(end_date)
            print("valid 2")


            for single_date in (start_date , end_date):
                date_range.append(single_date)
                print("valid 3")



            for day in date_range:
                    ds1 = DateAndSlot.objects.create(booking_date = day , booking_slot = "S1")
                    ds1.save()
                    ds2 = DateAndSlot.objects.create(booking_date = day , booking_slot = "S2")
                    ds2.save()
                    print("valid 4")

            form = DateRangeForm()
            return render(request , 'manager/addDates.html' , {'form': form })

    context = {
        'form': form ,
    }
    return render(request , 'manager/addDates.html' , context)
    '''

