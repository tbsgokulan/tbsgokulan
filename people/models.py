from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from common.common import Common

# Create your moModeldels here.
class Customer(Common):
    customer_name=models.CharField(max_length=120)
    customer_email=models.EmailField(max_length=120)
    customer_phone_no=PhoneNumberField('customer_phone_no')
    customer_country=models.CharField(max_length=110)
    customer_city=models.CharField(max_length=210)
    customer_address=models.CharField(max_length=220)
    def __str__(self):
        return str(self.customer_name)
class Supplier(Common):
    supplier_name=models.CharField(max_length=120)
    supplier_email=models.EmailField(max_length=120)
    supplier_phone_no=PhoneNumberField('supplier_phone_no')
    supplier_country=models.CharField(max_length=120)
    supplier_city=models.CharField(max_length=120)
    supplier_address=models.CharField(max_length=220)
    def __str__(self):
        return str(self.supplier_name)

