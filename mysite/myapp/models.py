from django.db import models

class Product(models.Model):
    name_prod = models.CharField(max_length=64)
    cost = models.IntegerField()

    def __str__(self):
        return f"{self.name_prod} : {self.cost}"
    '''class Meta():
        app_label = 'models.Product'''
    
    
    

class Customer(models.Model):
    name = models.CharField(max_length=64)
    money = models.IntegerField()

    def __str__(self):
        return f"{self.name} have {self.money} money"