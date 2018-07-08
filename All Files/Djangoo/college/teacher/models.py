from django.db import models


# Create your models here


class Teacher(models.Model):
    IdNo = models.CharField(max_length=8)
    Name = models.CharField(max_length=15)
    Department = models.CharField(max_length=10)

    def __str__(self):
        return self.IdNo + self.Name + self.Department
