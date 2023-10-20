from django.utils import timezone
from django.db import models

class Person (models.Model):
    id_person = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length= 200)
    second_name = models.CharField(max_length= 200)
    last_name = models.CharField(max_length=200)
    last_name2 = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.first_name} {self.second_name} {self.last_name} {self.last_name2} '
    
class Spent (models.Model):
    date_registered = models.DateField(default=timezone.now)
    hour_registered = models.TimeField(default=timezone.now)
    amount = models.IntegerField()
    type = models.CharField(max_length=200)
    observation = models.CharField(max_length=200)
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date_registered} {self.hour_registered} {self.amount} {self.type} {self.observation}'
    
class Income (models.Model):
    date_registered = models.DateField(default=timezone.now)
    hour_registered = models.TimeField(default=timezone.now)
    amount = models.IntegerField()
    type = models.CharField(max_length=200)
    observation = models.CharField(max_length=200)
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date_registered} {self.hour_registered} {self.amount} {self.type} {self.observation} '