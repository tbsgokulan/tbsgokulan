from django.db import models
from productapp.models import Product
from people.models import Supplier
from settingsapp.models import Warehouse
from common.common import Common
# Create your models here.
class Purchases_return(Common):
    STATUS=(('Completed','completed'),('Pending','pending'),)
    PAYMENT_STATUS=(('Paid','paid'),('Partial','partial'),('Unpaid','unpaid'),)

    purchases_return_additional_discount=models.IntegerField(default=0)
    purchases_return_date=models.CharField(max_length=30)
    purchases_return_additional_tax=models.IntegerField(default=0)
    purchases_return_grand_total=models.BigIntegerField()
    purchases_return_notes=models.TextField()
    purchases_return_shipping_charges=models.IntegerField(default=0)
    #purchases_product details
    purchases_return_status=models.CharField('status',max_length=50,choices=STATUS)
    purchases_return_supplier=models.ForeignKey(Supplier,related_name='purchases_return_supplier',on_delete=models.CASCADE)
    purchases_return_warehouse=models.ForeignKey(Warehouse,related_name='purchases_return_warehouse',on_delete=models.CASCADE)
    #list_purchases
    purchases_return_paid=models.BigIntegerField(default=0)
    purchases_return_due=models.BigIntegerField(default=0)
    purchases_return_payment_status=models.CharField('purchases_return_payment_status',max_length=50,choices=PAYMENT_STATUS,default='Unpaid')
    purchases_return_reference=models.CharField(max_length=50,blank=True,null=True)

class Purchases_return_purchase_detail(Common):
    
    purchases_return_purchase=models.ForeignKey(Purchases_return,related_name='purchases_return_purchase',on_delete=models.CASCADE)
    purchases_return_product_code=models.ForeignKey(Product,related_name='purchases_return_product',on_delete=models.CASCADE)
    purchases_return_product_cost=models.IntegerField()
    purchases_return_produt_stock=models.IntegerField()
    purchases_return_product_quantity=models.IntegerField()
    purchases_return_product_discount=models.IntegerField()
    purchases_return_product_tax=models.IntegerField()
    purchases_return_sub=models.IntegerField()
    
    def __str__(self):
        return str(self.purchases_return_product_code)
class payment_status(Common):
    pr_payment_purchase=models.ForeignKey(Purchases_return,related_name='payment_purchase_return',on_delete=models.CASCADE)
    pr_payment_date=models.CharField(max_length=50,blank=True,null=True)
    pr_payment_reference=models.CharField(max_length=50,blank=True,null=True)
    pr_payment_choice=models.CharField(max_length=50,blank=True,null=True)
    pr_payment_amount=models.BigIntegerField(default=0)
    pr_payment_due=models.BigIntegerField(default=0)
    pr_payment_note=models.TextField()    