
from re import S
from django.db import models
from common.common import Common
# from settingsapp.models import Brand, Category, Unit

# Create your models here.
class Product(Common):
    BARCODE_SYMBOLOGY= (('C', 'CODE128'), ('C1', 'CODE39'), ('E', 'EAN8'),)
    TAX_TYPE=(('I','INCLUSIVE'),('E','EXCLUSIVE'),)

    product_name=models.CharField(max_length=120)
    product_code=models.IntegerField(unique=True)
    category=models.ForeignKey('settingsapp.Category',related_name='category',on_delete=models.CASCADE)
    brand=models.ForeignKey('settingsapp.Brand',related_name='brand',on_delete=models.CASCADE)
    barcode_symbology=models.CharField('barcode_symbology',max_length=50,choices=BARCODE_SYMBOLOGY)
    product_cost=models.IntegerField()
    product_price=models.IntegerField()
    product_unit=models.ForeignKey('settingsapp.Unit',related_name='product_unit',on_delete=models.CASCADE)
    sale_unit=models.ForeignKey('settingsapp.Unit',related_name='sale_unit',on_delete=models.CASCADE)
    purchase_unit=models.ForeignKey('settingsapp.Unit',related_name='purchase_unit',on_delete=models.CASCADE)
    
    order_tax=models.IntegerField(default=0)
    tax_type=models.CharField('tax_type',max_length=50,choices=TAX_TYPE)
    note=models.CharField(max_length=255,blank=True,null=True)
    stock_alert=models.IntegerField()
    product_stock=models.IntegerField(default=0)
    product_image=models.TextField()
    product_quantity=models.IntegerField(default=0)
    product_discount=models.IntegerField(default=0)
    def __str__(self):
        return str(self.product_code)








    
    
        