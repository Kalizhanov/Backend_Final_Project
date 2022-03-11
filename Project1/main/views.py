from django.shortcuts import render
from .models import History, Mgp, Tradition


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def history(request):
    histr = History.objects.order_by('years')
    return render(request, 'main/history.html', {'histr': histr})

def trad(request):
    trad = Tradition.objects.all()
    return render(request, 'main/traditions.html', {'trad': trad})

def nature(request):
    return render(request, 'main/nature.html')

def megap(request):
    bcities = Mgp.objects.order_by('-population')
    return render(request, 'main/megapolises.html', {'city': bcities})

