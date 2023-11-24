from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import sys
sys.path.append('mysite/myapp/templates/myapp')

class FromForm(forms.Form):
    label = forms.CharField(label="Sign up")

def mainpage(request):
    return render(request,'myapp/mainpage.html',{'forms':FromForm()})

