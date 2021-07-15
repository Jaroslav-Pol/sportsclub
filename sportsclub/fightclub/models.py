from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Group(models.Model):
    name = models.CharField('Grupės pavadinimas', max_length=200, help_text='Įveskite grupės pavadinimą')
    week_day = models.CharField('Savaitės dienos', max_length=200, help_text='Įrašykite dienas, kuriomis '
                                                                                      'vyksta grupės treniruotės')
    start_time = models.CharField('Pradžios laikas', max_length=200)
    description = models.TextField('Aprašymas', max_length=1000, help_text='Trumpas aprašymas')

    def __str__(self):
        return f"{self.name}. {self.week_day} - {self.start_time}"

    class Meta:
        verbose_name = "Grupė"
        verbose_name_plural = "Grupės"

class Membership(models.Model):
    """Galimos narystės"""
    name = models.CharField('Narystės pavadinimas', max_length=200)
    price = models.FloatField('Mėnesio kaina')
    description = models.TextField('Aprašymas', max_length=1000)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Narystė"

class UserMembership(models.Model):
    """Modelis parodantis konkrėtaus vartotojo turimas narystes ir grupes"""
    member = models.ForeignKey(User, verbose_name='Narys', on_delete=models.SET_NULL, null=True, blank=True)
    membership = models.ForeignKey(Membership, verbose_name='Narystė', on_delete=models.SET_NULL, null=True, blank=True)
    group = models.ManyToManyField(Group, help_text='Pasirinkite grupes')

    def display_group(self):
        """Atvaizduoja grupes (dėl many to many lauko)"""
        return ', '.join(group.name for group in self.group.all()[:3])

    display_group.short_description = 'Grupė'

    def __str__(self):
        return f"{self.member}, narystė: {self.membership}"

    class Meta:
        verbose_name = "Vartotojo narystė"
        verbose_name_plural = "Vartotojų narystės"
