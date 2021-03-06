# Generated by Django 3.2.5 on 2021-07-14 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Įveskite grupės pavadinimą', max_length=200, verbose_name='Grupės pavadinimas')),
                ('week_day', models.CharField(help_text='Įrašykite dienas, kuriomis vyksta grupės treniruotės', max_length=200, verbose_name='Vyksta savaitės dienomis')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='Pradžios laikas')),
            ],
        ),
    ]
