from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"Profile({self.user.username})"

class TravelOption(models.Model):
    TYPE_CHOICES = [("Flight", "Flight"), ("Train", "Train"), ("Bus", "Bus")]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.PositiveIntegerField()

    class Meta:
        ordering = ["date_time"]

    def __str__(self):
        return f"{self.type}: {self.source} → {self.destination} @ {self.date_time:%Y-%m-%d %H:%M}"

class Booking(models.Model):
    STATUS_CHOICES = [("Confirmed", "Confirmed"), ("Cancelled", "Cancelled")]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    travel_option = models.ForeignKey(TravelOption, on_delete=models.CASCADE)
    num_seats = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Confirmed")

    class Meta:
        ordering = ["-booking_date"]

    def __str__(self):
        return f"Booking {self.pk} by {self.user.username}"
