# Generated by Django 4.0.3 on 2022-03-03 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mgp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('population', models.CharField(max_length=30, verbose_name='Population')),
                ('area', models.CharField(max_length=50, verbose_name='Area')),
                ('place', models.TextField(verbose_name='Location')),
            ],
        ),
    ]
