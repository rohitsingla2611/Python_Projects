from django.db import models


# Create your models here.

class Classroom(models.Model):
    RoomNo = models.CharField(max_length=4)
    Seats = models.CharField(max_length=4)
    AllottedTo = models.CharField(max_length=20)

    def __str__(self):
        return self.RoomNo, self.Seats, self.AllottedTo
