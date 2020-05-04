from django.db import models

class Airport(models.Model):
    code=models.CharField(max_length=50)
    city=models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.city} ({self.code})"
    
class Flight(models.Model):
    origin=models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination=models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration=models.IntegerField()

    def __str__(self):
        return f"{self.origin} - {self.destination} to {self.duration}"
 
class Passenger(models.Model):
     first =models.CharField(max_length =64)
     last =models.CharField(max_length=64)
     flights=models.ManyToManyField(Flight, blank=True, related_name='passengers')

     def __str__(self):
         return f"{self.first} {self.last}"
     