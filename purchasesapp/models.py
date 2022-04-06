from re import sub
from django.db import models
from common.common import Common
from people.models import Supplier
from productapp.models import Product
from settingsapp.models import Warehouse
# Create your models here.
class Purchase(Common):
    STATUS=(('Ordered','ordered'),('Received','received'),('Pending','pending'),)
    PAYMENT_STATUS=(('Paid','paid'),('Partial','partial'),('Unpaid','unpaid'),)

    additional_discount=models.IntegerField(default=0)
    date=models.CharField(max_length=30)
    additional_tax=models.IntegerField(default=0)
    grand_total=models.BigIntegerField()
    notes=models.TextField()
    shipping_charges=models.IntegerField(default=0)
    product=models.ForeignKey(Product,related_name='product',on_delete=models.CASCADE, blank=True,null=True)
    #purchases_product details
    status=models.CharField('status',max_length=50,choices=STATUS)
    supplier=models.ForeignKey(Supplier,related_name='Supplier',on_delete=models.CASCADE)
    warehouse=models.ForeignKey(Warehouse,related_name='warehouse',on_delete=models.CASCADE)
    #list_purchases
    paid=models.BigIntegerField(default=0)
    due=models.BigIntegerField(default=0)
    payment_status=models.CharField('payment_status',max_length=50,choices=PAYMENT_STATUS,default='Unpaid')
    reference=models.CharField(max_length=50,blank=True,null=True)
    # def save(self,*args,**kwargs):
    #     if self.payment_status == 'unpaid':
    #         a=["%04d" % x for x in range(10000)]
    #         id=
    #         value="PR_{}".format(a[id])
    #         self.reference=value
    #     super().save(*args,**kwargs)

class purchase_detail(Common):
    
    purchase=models.ForeignKey(Purchase,related_name='Purchase',on_delete=models.CASCADE)
    product_code=models.ForeignKey(Product,related_name='Product',on_delete=models.CASCADE)
    product_cost=models.IntegerField()
    produt_stock=models.IntegerField()
    product_quantity=models.IntegerField()
    product_discount=models.IntegerField()
    product_tax=models.IntegerField()
    sub=models.IntegerField()
    def __str__(self):
        return str(self.product_code)   
class payment_status(Common):
    payment_purchase=models.ForeignKey(Purchase,related_name='payment_Purchase',on_delete=models.CASCADE)
    payment_date=models.CharField(max_length=50,blank=True,null=True)
    payment_reference=models.CharField(max_length=50,blank=True,null=True)
    payment_choice=models.CharField(max_length=50,blank=True,null=True)
    payment_amount=models.BigIntegerField(default=0)
    payment_due=models.BigIntegerField(default=0)
    payment_note=models.TextField()

    

    