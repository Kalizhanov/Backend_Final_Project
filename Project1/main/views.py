from multiprocessing import context
import re
from urllib import response
from django.shortcuts import redirect, render, get_object_or_404
from .models import History, Mgp, Presidents, Tradition, Registration
from .forms import TraditionForm, RegistrationForm #did import of form and redirect
from django.core.mail import *


def index(request):
    return render(request, 'main/index.html')

def about_us(request):
    return render(request, 'main/about.html')

def aboutG(request):
    return render(request, 'main/aboutG.html')

def aboutA(request):
    return render(request, 'main/aboutA.html')

def aboutY(request):
    return render(request, 'main/aboutY.html')

def history(request):
    histr = History.objects.order_by('years')
    return render(request, 'main/history.html', {'histr': histr})

def trad(request):
    trad = Tradition.objects.all()
    return render(request, 'main/traditions.html', {'trad': trad})

def nature(request):
    return render(request, 'main/nature.html')

def megap(request):
    bcities = Mgp.objects.order_by('id')
    return render(request, 'main/megapolises.html', {'city': bcities})

#here creating method insert
def insert(request):
    form = TraditionForm()
    if request.method == 'POST':
        print('h')
        form = TraditionForm(request.POST)
        if form.is_valid():
            print('l')
            form.save()
            return redirect('/traditions')
    context = {'form': form}
    return render(request, 'main/insert.html', context)
#ending creating method insert

#here updating method 
def update(request, pk):
    trad =  Tradition.objects.get(id=pk)
    form = TraditionForm(instance=trad)
    if request.method == 'POST':
        form = TraditionForm(request.POST, instance=trad)
        if form.is_valid():
            form.save()
            return redirect('/traditions')
    context = {'form': form}
    return render(request, 'main/insert.html', context)
#end of updating method

def delete(request, pk):
    trad = Tradition.objects.get(id=pk)
    if request.method == 'POST':
        trad.delete()
        return redirect('/traditions')
    context = {'item':trad}
    return render(request, 'main/delete.html', context)

def details(request, slug):
    trad = Tradition.objects.get(slug=slug)
    context = {'items':trad}
    return render(request, 'main/details.html', context)


def reg(request):
    form = RegistrationForm()
    to_email = ''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            to_email = form.cleaned_data.get("email")
            send_mail("Kazakhstan.kz", "Nothing. I'm just checking this function!!!", "200103260@stu.sdu.edu.kz", [to_email], fail_silently=False, html_message="<b>You registered to Kazakhstan.kz</b>")
            return redirect('/send')
    return render(request, 'main/login.html', {'form' : form})

def send_message(request):
    # email = EmailMessage(
    #     'Checking a file',
    #     'In this message I am checking a file',
    #     '200103260@stu.sdu.edu.kz',
    #     ['galymzhanks@gmail.com', '200103260@stu.sdu.edu.kz']
    # )
    # email.attach_file('/Users/Galymzhan/Desktop/uchebniki/Turkish/gelecek zaman.docx')
    # email.send(fail_silently=False)
    return render(request, "main/successfull.html")     


def pres(request):
    return render(request, 'main/pres.html')

def show_post(request, post_slug):
    post = get_object_or_404(Presidents, slug = post_slug)
    return render(request, 'main/Slug.html', {'post':post})