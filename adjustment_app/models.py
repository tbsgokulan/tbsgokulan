from operator import mod
from django.db import models
from common.common import Common
from settingsapp.models import Warehouse

# Create your models here.
ADJ_STATUS=(('Addition','addition'),('Subtraction','subtraction'))
class Adjustment(Common):
    adj_date=models.CharField(max_length=40)
    adj_reference=models.CharField(max_length=100,blank=True,null=True)
    adj_warehouse=models.ForeignKey(Warehouse,related_name='adjustment_warehouse',on_delete=models.CASCADE)
    adj_note=models.TextField()
    adj_total_product=models.IntegerField(default=0)

class Adjustment_detail(Common):
    adj_header=models.ForeignKey(Adjustment,related_name='adj_detail',on_delete=models.CASCADE)
    adj_product_code=models.BigIntegerField()
    adj_product_name=models.CharField(max_length=100)
    adj_stock=models.BigIntegerField(default=0)
    adj_quantity=models.BigIntegerField(default=0)
    adj_type=models.CharField('adj_type',max_length=15,choices=ADJ_STATUS,default='Addition')
