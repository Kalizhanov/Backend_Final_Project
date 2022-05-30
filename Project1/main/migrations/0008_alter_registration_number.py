# Generated by Django 4.0.3 on 2022-04-14 10:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_registration_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='number',
            field=models.CharField(blank=True, max_length=11, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{7,11}$')], verbose_name='Phone Number'),
        ),
    ]