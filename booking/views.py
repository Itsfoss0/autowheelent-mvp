from django.shortcuts import render
from django.contrib import messages
from cars.models import Car
from booking.models import Booking

def booking(request):
    cars = Car.objects.order_by('-created_date')

    data = {
        'cars': cars
    }
    return render(request, 'booking/booking.html', data)


def create_booking(request):
    """
    Create a new booking
    """
    if request.method == "POST":
        selected_car_id = request.POST.get('car')
        selected_car = Car.objects.get(id=selected_car_id)
        pickup_location = request.POST.get('pickup_location')
        dropoff_location = request.POST.get('dropoff_location')
        booking_date = request.POST.get('booking_date')

        booking = Booking(
            user=request.user,
            pickup_location=pickup_location,
            dropoff_location=dropoff_location,
            car=selected_car
        )
        booking.save()
        messages.success(request, 'Booking Created')