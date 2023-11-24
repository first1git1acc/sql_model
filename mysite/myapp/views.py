from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import sys
from django.urls import reverse
from django.http import HttpResponseRedirect

sys.path.append('mysite/myapp/templates/myapp')

class FromForm(forms.Form):
    email = forms.CharField(label="email")
    password = forms.CharField(label="password",widget=forms.PasswordInput())



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
            request.session["eml"] += em_l
            return HttpResponseRedirect(reverse("myapp:add"))
        else:
            return render(request,'myapp/mainpage.html',{'form':FromForm()})

    return render(request,'myapp/mainpage.html',{'form':FromForm()})

def add(request):
    if "pas" not in request.session:
        request.session["pas"] = []
    if "eml" not in request.session:
        request.session["eml"] = []
    return render(request,'myapp/add.html',{
        "pas":request.session["pas"],
        "eml":request.session["eml"]})

