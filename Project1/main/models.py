from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse

class History (models.Model):
    years = models.IntegerField('Years')
    hap = models.TextField('What happened')

    def __str__(self):
        return str(self.years)


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
    slug = models.SlugField(null=False, default='naruto', unique=True)
    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.tradition


class Registration (models.Model):
    first_name = models.CharField('First Name', max_length=50)
    second_name = models.CharField('Second Name', max_length=50)
    age = models.IntegerField('Age')
    username = models.CharField('Username', max_length=50)
    password = models.CharField('Password', max_length=50)
    email = models.EmailField('Email')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{7,11}$')
    number = models.CharField("Phone Number", validators=[phone_regex], max_length=11, blank=True)

    def __str__(self):
        return self.first_name

    def get_boolean(self):
        return True

class Presidents(models.Model):
    name = models.CharField(max_length=255)
    years = models.CharField(max_length=10)
    describe = models.TextField(default='There\'s some infromations')
    image = models.CharField(max_length=1500, default='disco')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug':self.slug})

    class Meta:
        verbose_name='Президент'
        verbose_name_plural='Президенттер'