# Generated by Django 4.0.3 on 2022-05-23 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_tradition_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presidents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('years', models.CharField(max_length=10)),
                ('describe', models.TextField(default="There's some infromations")),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Мақала',
                'verbose_name_plural': 'Мақалалар',
            },
        ),
    ]
