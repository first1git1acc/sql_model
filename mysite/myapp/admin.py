from django.contrib import admin
import sys

sys.path.append('D:/sql_model/mysite/myapp')

from myapp.models import Customer,Product,State

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(State)
# Register your models here.
