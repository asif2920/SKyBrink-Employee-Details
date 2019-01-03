from django.db import models

# Create your models here.

class Employee(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    employeeid = models.IntegerField()

    def __str__(self):
        return self.firstname