from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Group(models.Model):
    name = models.CharField('Grupės pavadinimas', max_length=200, help_text='Įveskite grupės pavadinimą')
    week_day = models.CharField('Vyksta savaitės dienomis', max_length=200, help_text='Įrašykite dienas, kuriomis '
                                                                                      'vyksta grupės treniruotės')
    start_time = models.CharField('Pradžios laikas', max_length=200)
    description = models.TextField('Aprašymas', max_length=1000, help_text='Trumpas aprašymas')

    def __str__(self):
        return f"{self.name}. {self.week_day} - {self.start_time}"


class Membership(models.Model):
    name = models.CharField('Narystės pavadinimas', max_length=200)
    price = models.FloatField('Mėnesio kaina')
    description = models.TextField('Aprašymas', max_length=1000)

    def __str__(self):
        return f"{self.name}: {self.description}. Kaina:{self.price}"


class UserMembership(models.Model):
    member = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True, blank=True)
    group = models.ManyToManyField(Group, help_text='Pasirinkite grupes')

    def __str__(self):
        return f"{self.member}, narystė: {self.membership}"


