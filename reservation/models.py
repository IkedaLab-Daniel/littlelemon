from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guest = models.SmallIntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.name + ' , ' + str(self.no_of_guest)+ ' guesses' + ' , ' + str(self.booking_date)

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    inventory = models.BooleanField()

    def __str__(self):
        return 'name: ' + self.title + ', price: ' + str(self.price) + ', stock: ' + str(self.inventory)