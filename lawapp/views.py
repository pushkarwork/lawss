from django.shortcuts import render
from .models import Practise, Contact
# Create your views here.


def index(request):
    practises = Practise.objects.all()
    return render(request, 'index.html', {'practises': practises})


def contact(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        inst = Contact(firstname=firstname, lastname=lastname,
                       email=email, phone=phone, message=message)
        inst.save()
    return render(request, 'contact.html')
