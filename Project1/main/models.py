from django.db import models

class History (models.Model):
    years = models.IntegerField('Years')
    hap = models.TextField('What happened')

    def __str__(self):
        return self.years


class Mgp (models.Model):
    city = models.CharField('City', max_length=50)
    population = models.CharField('Population', max_length=30)
    area = models.CharField('Area', max_length=50)
    place = models.TextField('Location')

    def __str__(self):
        return self.city


class Tradition (models.Model):
    tradition = models.CharField('Tradition', max_length=50)
    descr = models.TextField('Description')

    def __str__(self):
        return self.tradition