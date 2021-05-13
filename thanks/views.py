import json
from django.shortcuts import render, redirect
from .forms import CustomerForm
from django.http import HttpResponse
from django.contrib import messages
from .models import customer

# from django.http import HttpResponse
# from thanks.forms import UserForm


def index(request):
    if request.method == 'POST':
        data = request.POST
        # assert False, data["name"]
        name, message = data["name"], data["message"]
        
        #     message = "Message saved successfully!"
        # else:
        #     message = 'Message not saved!'
        a = customer(name=name, message=message)
        a.save()
        response = {"message": "success"}
        return HttpResponse( json.dumps(response ) )


def home(request):
    b = customer.objects.order_by('-id')[:6]
    # c = customer.objects.last()
    # assert False, c
    context = {'ash' : b}
    return render(request, "home.html", context)

def last(request):
    c = customer.objects.last()
    # assert False, c
    context = {'name' : c}
    return render(request, "base.html", context)