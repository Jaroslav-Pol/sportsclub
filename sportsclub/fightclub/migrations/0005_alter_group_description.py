# Generated by Django 3.2.5 on 2021-07-15 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fightclub', '0004_auto_20210715_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(help_text='Trumpas aprašymas', max_length=1000, verbose_name='Aprašymas'),
        ),
    ]
