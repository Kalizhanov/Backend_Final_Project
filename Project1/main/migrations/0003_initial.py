# Generated by Django 4.0.3 on 2022-03-03 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_delete_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years', models.IntegerField(verbose_name='Years')),
                ('hap', models.TextField(verbose_name='What happened')),
            ],
        ),
    ]
