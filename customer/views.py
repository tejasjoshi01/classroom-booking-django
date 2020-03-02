from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse , Http404

from .forms import CustomerBookingForm
from manager.models import DateAndSlot 
from .models import CustomerBooking

  
def customerDashboard(request):  
    date_slot_list = DateAndSlot.objects.all().order_by('-booking_date')
    content = {
            'date_slot_list' : date_slot_list
        }
    return render(request,"customer/customerDashboard.html",content) 


def customerRoomBooking(request, slot_id):
    try:
            selected_date_slot = DateAndSlot.objects.get(pk=slot_id)
            booking  = CustomerBooking()
            booking.booking_date_slot = selected_date_slot            
            booking.bookee_username = request.user.username 
            form = CustomerBookingForm(request.POST , instance = booking )

            if form.is_valid():
                form.save()
                form = CustomerBookingForm()

    except DateAndSlot.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request,"customer/customerRoomBooking.html" , {'form':form})


def getUserBookings(request):
    user_booking_list = CustomerBooking.objects.filter(bookee_username = request.user)
    content = {
            'user_booking_list' : user_booking_list
        }

    return render(request , 'customer/userBookings.html' , content)