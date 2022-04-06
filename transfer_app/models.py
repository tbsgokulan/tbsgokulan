from telnetlib import STATUS
from django.db import models
from productapp.models import Product
from common.common import Common
from settingsapp.models import Warehouse

# Create your models here.
class Transfer(Common):
    SALES_STATUS=(('Sent','sent'),('Completed','completed'),('Pending','pending'),)
    
    tr_date=models.CharField(max_length=30)
    tr_from_warehouse=models.ForeignKey(Warehouse,related_name='tr_warehouse',on_delete=models.CASCADE )
    tr_to_warehouse=models.ForeignKey(Warehouse,related_name='tr_to_warehouse',on_delete=models.CASCADE)
    tr_additional_tax=models.IntegerField(default=0)
    tr_additional_discount=models.IntegerField(default=0)
    tr_grand_total=models.BigIntegerField()
    tr_reference=models.CharField(max_length=50,blank=True,null=True)
    tr_shipping_charges=models.IntegerField(default=0)
    tr_status=models.CharField('tr_status',max_length=15,choices=SALES_STATUS,default='Pending')
    tr_notes=models.TextField()
    tr_total_product=models.IntegerField(default=0)

class Transfer_detail(Common):
    tr_purchase=models.ForeignKey(Transfer,related_name='tr',on_delete=models.CASCADE)
    tr_product_code=models.ForeignKey(Product,related_name='tr_product',on_delete=models.CASCADE)
    tr_product_cost=models.IntegerField()
    tr_product_stock=models.IntegerField()
    tr_product_quantity=models.IntegerField()
    tr_product_discount=models.IntegerField()
    tr_product_tax=models.IntegerField()
    tr_sub=models.IntegerField()
    def __str__(self):
        return str(self.tr_product_code)
