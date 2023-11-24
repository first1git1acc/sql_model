from django.urls import path
import sys

sys.path.append("D:\sql_model\mysite\myapp")
import views

urlpatterns = [
    path("",views.index,name="index")
]