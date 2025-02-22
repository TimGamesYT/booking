from django.shortcuts import render
from .models import Room, Booking
from django.http import HttpResponse

# Create your views here.
def room_list(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms,
    }

    return render(request, 'booking/room-list.html', context)

def room_details(request, pk):
    room = Room.objects.get(id=pk)
    context = {
        "room": room
    }

    return render(request, 'booking/room-details.html', context)

def book_room(request):
    if request.method== "POST":
        room_number = request.POST.get("room-number")
        start_time = request.POST.get("start-time")
        end_time = request.POST.get("end-time")
        try:
            room = Room.objects.get(number = room_number)
        except Room.DoesNotExist:
            return HttpResponse("not exist", status=404)

        booking = Booking.objects.create(
            user=request.user,
            room=room,
            start_time=start_time,
            end_time=end_time,
        )
        return HttpResponse("room booked")
    else:
        return render(request, "booking/booking-form.html")