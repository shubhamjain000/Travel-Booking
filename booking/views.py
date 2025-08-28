from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import TravelOption, Booking, Profile
from .forms import RegisterForm, ProfileForm, TravelFilterForm, BookingForm

def travel_list(request):
    qs = TravelOption.objects.all()
    form = TravelFilterForm(request.GET or None)
    if form.is_valid():
        t = form.cleaned_data.get("type")
        src = form.cleaned_data.get("source")
        dst = form.cleaned_data.get("destination")
        dt = form.cleaned_data.get("date")
        if t:
            qs = qs.filter(type=t)
        if src:
            qs = qs.filter(source__icontains=src.strip())
        if dst:
            qs = qs.filter(destination__icontains=dst.strip())
        if dt:
            qs = qs.filter(date_time__date=dt)
    return render(request, "travel_list.html", {"travels": qs, "form": form})

@login_required
def book_travel(request, travel_id):
    travel = get_object_or_404(TravelOption, pk=travel_id)
    if travel.date_time < timezone.now():
        messages.error(request, "You cannot book a past travel option.")
        return redirect("travel_list")

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            seats = form.cleaned_data["num_seats"]
            if seats > travel.available_seats:
                messages.error(request, f"Only {travel.available_seats} seats left.")
            else:
                total = travel.price * seats
                Booking.objects.create(
                    user=request.user,
                    travel_option=travel,
                    num_seats=seats,
                    total_price=total,
                )
                travel.available_seats -= seats
                travel.save()
                messages.success(request, "Booking confirmed!")
                return redirect("my_bookings")
    else:
        form = BookingForm()

    return render(request, "booking_form.html", {"travel": travel, "form": form})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, "my_bookings.html", {"bookings": bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    if booking.status == "Cancelled":
        messages.info(request, "This booking is already cancelled.")
        return redirect("my_bookings")
    travel = booking.travel_option
    travel.available_seats += booking.num_seats
    travel.save()
    booking.status = "Cancelled"
    booking.save()
    messages.success(request, "Booking cancelled. Seats restored.")
    return redirect("my_bookings")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Welcome! Account created.")
            return redirect("travel_list")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})

@login_required
def profile(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect("profile")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = ProfileForm(instance=profile)
    return render(request, "registration/profile.html", {"form": form})
