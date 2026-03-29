from django.db import models


class Tour(models.Model):
    title = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.PositiveIntegerField()
    image = models.ImageField(upload_to='tours/', blank=True, null=True)
    available_slots = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='bookings')
    client_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    people_count = models.PositiveIntegerField(default=1)
    travel_date = models.DateField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.tour.title}"