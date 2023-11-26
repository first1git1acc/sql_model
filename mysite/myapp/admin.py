from django.contrib import admin
import sys

sys.path.append('D:/sql_model/mysite/myapp')

from myapp.models import Customer,Product

admin.site.register(Product)
admin.site.register(Customer)

# Register your models here.
