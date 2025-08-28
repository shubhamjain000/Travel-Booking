from django.contrib import admin
from .models import TravelOption, Booking, Profile

@admin.register(TravelOption)
class TravelOptionAdmin(admin.ModelAdmin):
    list_display = ("id", "type", "source", "destination", "date_time", "price", "available_seats")
    list_filter = ("type", "source", "destination")
    search_fields = ("source", "destination")

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "travel_option", "num_seats", "total_price", "status", "booking_date")
    list_filter = ("status",)
    search_fields = ("user__username", "travel_option__source", "travel_option__destination")

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone")
