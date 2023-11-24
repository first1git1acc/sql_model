from django.urls import path
import sys

sys.path.append("D:/sql_model/mysite/myapp")
import views

app_name = 'myapp'

urlpatterns = [
    path("",views.mainpage,name="mainpage")
]