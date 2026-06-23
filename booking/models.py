from django.db import models
from django.contrib.auth.models import User

class Court(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('maintenance', 'Under Maintenance'),
    ]
    COURT_TYPES = [
        ('indoor', 'Indoor'),
        ('outdoor', 'Outdoor'),
    ]
    
    name = models.CharField(db_index=True, max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    court_type = models.CharField(max_length=20, choices=COURT_TYPES, default='indoor')

    def __str__(self):
        return f"{self.name} ({self.get_court_type_display()})"

class Booking(models.Model):
    BOOKING_STATUS = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    court = models.ForeignKey(Court, on_delete=models.CASCADE, related_name='bookings')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=BOOKING_STATUS, default='confirmed')

    def __str__(self):
        return f"Booking {self.id} - {self.court.name} by {self.user.username}"