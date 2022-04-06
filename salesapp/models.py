from telnetlib import STATUS
from django.db import models
from productapp.models import Product
from common.common import Common
from people.models import Customer
from settingsapp.models import Warehouse

# Create your models here.
class Sales(Common):
    SALES_STATUS=(('ORDERED','ordered'),('COMPLETED','completed'),('PENDING','pending'),)
    SALES_PAYMENT_STATUS=(('PAID','Paid'),('PARTIAL','partial'),('Unpaid','unpaid'),)
    
    sales_date=models.CharField(max_length=30)
    sales_customer=models.ForeignKey(Customer,related_name='sales_Customer',on_delete=models.CASCADE )
    sales_warehouse=models.ForeignKey(Warehouse,related_name='sales_Warehouse',on_delete=models.CASCADE)
    sales_additional_tax=models.IntegerField(default=0)
    sales_additional_discount=models.IntegerField(default=0)
    sales_paid=models.BigIntegerField(default=0)
    sales_due=models.BigIntegerField(default=0)
    sales_grand_total=models.BigIntegerField()
    sales_reference=models.CharField(max_length=50,blank=True,null=True)
    sales_shipping_charges=models.IntegerField(default=0)
    sales_status=models.CharField('sales_status',max_length=15,choices=SALES_STATUS,default='PENDING')
    sales_payment_status=models.CharField('sales_payment_status',max_length=15,choices=SALES_PAYMENT_STATUS,default='Unpaid')
    sales_notes=models.TextField()

class Sales_detail(Common):
    sales_purchase=models.ForeignKey(Sales,related_name='sales_sales',on_delete=models.CASCADE)
    sales_product_code=models.ForeignKey(Product,related_name='sales_Product',on_delete=models.CASCADE)
    sales_product_cost=models.IntegerField()
    sales_product_stock=models.IntegerField()
    sales_product_quantity=models.IntegerField()
    sales_product_discount=models.IntegerField()
    sales_product_tax=models.IntegerField()
    sales_sub=models.IntegerField()
    def __str__(self):
        return str(self.sales_product_code)
class Sales_payment_status(Common):
    sales_payment_purchase=models.ForeignKey(Sales,related_name='payment_sales',on_delete=models.CASCADE)
    sales_payment_date=models.CharField(max_length=50,blank=True,null=True)
    sales_payment_reference=models.CharField(max_length=50,blank=True,null=True)
    sales_payment_choice=models.CharField(max_length=50,blank=True,null=True)
    sales_payment_amount=models.BigIntegerField(default=0)
    sales_payment_due=models.BigIntegerField(default=0)
    sales_payment_note=models.TextField()