from unicodedata import category
from django.db import models
from common.common import Common

from settingsapp.models import Warehouse

# Create your models here.
class Expenses_category(Common):
    expenses_category_name=models.CharField(max_length=50,blank=True)
    expenses_description=models.TextField()
    def __str__(self):
        return str(self.expenses_category_name)
class Expenses(Common):
    expensescategory=models.ForeignKey(Expenses_category,on_delete=models.CASCADE,blank=True,null=True,related_name='exp_category')
    expenses_reference=models.CharField(max_length=100,blank=True)
    expenses_date=models.CharField(max_length=50)
    expenses_detail=models.TextField()
    expenses_amount=models.BigIntegerField()
    expenses_warehouse=models.ForeignKey(Warehouse,related_name='expense_Warehouse',on_delete=models.CASCADE)
    def __str__(self):
        return str(self.expensescategory)
