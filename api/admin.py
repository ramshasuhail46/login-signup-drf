from django.contrib import admin

# Register your models here.

from .models import User, Passenger, Flight, Seat, Reservation


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('email', 'username', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username', 'is_active',)
    ordering = ('email',)


class PassengerAdmin(admin.ModelAdmin):
    model = Passenger
    list_display = ('user', 'first_name', 'last_name',
                    'passport_number', 'dob',)
    search_fields = ('passport_number', 'user',)


class FlightAdmin(admin.ModelAdmin):
    model = Flight
    list_display = ('flight_number', 'departure_location', 'arrival_location',
                    'airline', 'aircraft', 'flight_duration', 'departure_time',)
    search_fields = ('flight_number', 'departure_location',
                     'arrival_location', 'airline', 'departure_time')
    ordering = ('flight_number',)


class SeatAdmin(admin.ModelAdmin):
    model = Seat
    list_display = ('flight', 'seat_number', 'seat_class', 'is_available',)
    search_fields = ('flight', 'seat_class', 'is_available')


class ReservationAdmin(admin.ModelAdmin):
    model = Reservation
    list_display = ('flight', 'passenger', 'seat', 'reservation_date','status',)
    search_fields = ('status', 'flight', 'passenger','reservation_date',)


admin.site.register(User, UserAdmin)
admin.site.register(Passenger, PassengerAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(Reservation, ReservationAdmin)
