from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import sys
from django.urls import reverse
from django.http import HttpResponseRedirect

sys.path.append('mysite/myapp/templates/myapp')
sys.path.append('D:/sql_model/mysite/myapp/static/styles')
sys.path.append('D:/sql_model/mysite/myapp')

from myapp.models import Customer,Product,State

class FromForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={
       'id':'second',
       'title':'Enter email',
       'placeholder':'Enter email ...' 
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'id':'first',
        'title':'Enter password',
        'placeholder':'Enter password ...'
        }))



def mainpage(request):
    if "pas" not in request.session:
        request.session["pas"] = []
    if "eml" not in request.session:
        request.session["eml"] = []
    if request.method == "POST":
        form = FromForm(request.POST)
        if form.is_valid():
            pa = form.cleaned_data["password"]
            request.session["pas"] += [pa]
            em_l = form.cleaned_data["email"]
            request.session["eml"] += [em_l]
            return HttpResponseRedirect(reverse('myapp:add'))
        else:
            return render(request,'myapp/mainpage.html',{'form':FromForm()})

    return render(request,'myapp/mainpage.html',{'form':FromForm()})

def add(request):
    if "pas" not in request.session:
        request.session["pas"] = []
    if "eml" not in request.session:
        request.session["eml"] = []
    
    zip_pas_eml = zip(request.session["pas"],request.session["eml"])
    return render(request,'myapp/add.html',{'vars':zip_pas_eml})

def myshop(request):
    return render(request,'myapp/myshop.html',{
        "customers":Customer.objects.all(),
        "products":Product.objects.all(),
    })

def createState(request):
    return render(request,'myapp/states.html',{
        "states":State.objects.all(),
    })
