from django.forms import ModelForm
from .models import Tradition, Registration


class TraditionForm(ModelForm):
    class Meta():
         model = Tradition
         fields = ['tradition', 'descr']


class RegistrationForm(ModelForm):
    class Meta():
        model = Registration
        fields = '__all__'
        