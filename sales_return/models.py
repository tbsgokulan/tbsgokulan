
from telnetlib import STATUS
from django.db import models
from productapp.models import Product
from common.common import Common
from people.models import Customer
from settingsapp.models import Warehouse

# Create your models here.
class Sales_return(Common):
    SALES_STATUS=(('Ordered','ordered'),('Completed','completed'),('Pending','pending'),)
    SALES_PAYMENT_STATUS=(('Paid','Paid'),('Partial','partial'),('Unpaid','unpaid'),)
    
    sr_date=models.CharField(max_length=30)
    sr_customer=models.ForeignKey(Customer,related_name='sr_customer',on_delete=models.CASCADE )
    sr_warehouse=models.ForeignKey(Warehouse,related_name='sr_warehouse',on_delete=models.CASCADE)
    sr_additional_tax=models.IntegerField(default=0)
    sr_additional_discount=models.IntegerField(default=0)
    sr_paid=models.BigIntegerField(default=0)
    sr_due=models.BigIntegerField(default=0)
    sr_grand_total=models.BigIntegerField()
    sr_reference=models.CharField(max_length=50,blank=True,null=True)
    sr_shipping_charges=models.IntegerField(default=0)
    sr_status=models.CharField('sr_status',max_length=15,choices=SALES_STATUS,default='Pending')
    sr_payment_status=models.CharField('sr_payment_status',max_length=15,choices=SALES_PAYMENT_STATUS,default='Unpaid')
    sr_notes=models.TextField()

class Sales_return_detail(Common):
    sr_purchase=models.ForeignKey(Sales_return,related_name='sr_sales',on_delete=models.CASCADE)
    sr_product_code=models.ForeignKey(Product,related_name='sr_product',on_delete=models.CASCADE)
    sr_product_cost=models.IntegerField()
    sr_product_stock=models.IntegerField()
    sr_product_quantity=models.IntegerField()
    sr_product_discount=models.IntegerField()
    sr_product_tax=models.IntegerField()
    sr_sub=models.IntegerField()
    def __str__(self):
        return str(self.sr_product_code)
class Sales_return_payment_status(Common):
    sr_payment_purchase=models.ForeignKey(Sales_return,related_name='sr_payment_sales',on_delete=models.CASCADE)
    sr_payment_date=models.CharField(max_length=50,blank=True,null=True)
    sr_payment_reference=models.CharField(max_length=50,blank=True,null=True)
    sr_payment_choice=models.CharField(max_length=50,blank=True,null=True)
    sr_payment_amount=models.BigIntegerField(default=0)
    sr_payment_due=models.BigIntegerField(default=0)
    sr_payment_note=models.TextField()
