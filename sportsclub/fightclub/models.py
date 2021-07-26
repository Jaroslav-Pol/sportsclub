from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Group(models.Model):
    """Galimos grupės"""
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
        verbose_name = "Kliento narystė"
        verbose_name_plural = "Klientų narystės"


class SportTest(models.Model):
    name = models.CharField('Testo pavadinimas', max_length=200)
    result_exp = models.CharField('Pažengusio rezultato slenkstis', max_length=200)
    result_sport = models.CharField('Sportinio rezultato slenkstis', max_length=200)
    description = models.TextField('Aprašymas', max_length=1000)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Sportinis testas"
        verbose_name_plural = "Sportiniai testai"


class UserSportResult(models.Model):
    name = models.ForeignKey(SportTest, verbose_name='Testas', on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, verbose_name='Narys', on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField('Atlikimo data', null=True, blank=True)
    result = models.CharField('Rezultatas', max_length=200)
    comment = models.TextField('Komentaras', max_length=1000)

    def __str__(self):
        return f"{self.name}, narys: {self.user}, data: {self.date}, rezultatas: {self.result}"

    class Meta:
        verbose_name = "Kliento sportinis rezultatas"
        verbose_name_plural = "Klientų sportiniai rezultatai"


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name='Vartotojas', on_delete=models.CASCADE)
    phone_nr = models.CharField('Telefono numeris', max_length=20, null=True, blank=True)
    birth_date = models.DateField('Gimimo data', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = "Kliento profilis"
        verbose_name_plural = "Klientų profiliai"
