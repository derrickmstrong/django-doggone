from django.db import models

class LostPet(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=30, blank=True)
    lost_date = models.DateTimeField()
    description = models.TextField(blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    age = models.IntegerField(null=True)
    siblings = models.ManyToManyField('Siblings', blank=True)

class Siblings(models.Model):
    name = models.CharField(max_length=100)