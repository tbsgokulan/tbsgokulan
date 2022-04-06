from django.db import models
from django.contrib.auth.models import User

from common.common import Common
from productapp.models import Product
# Create your models here.

class Warehouse(Common):
    warehouse_name=models.CharField(max_length=120)
    warehouse_phone=models.CharField(max_length=120)
    warehouse_country=models.CharField(max_length=120)
    warehouse_city=models.CharField(max_length=120)
    warehouse_email=models.EmailField(max_length=220)
    warehouse_zipcode=models.CharField(max_length=120)
    def __str__(self):
        return str(self.warehouse_name)
        #return f"{self.firstName} {self.secondName}"

class Warehouse_detail(Common):
    warehouse=models.ForeignKey(Warehouse,related_name='warehouseid',on_delete=models.CASCADE)
    product_code=models.ForeignKey(Product,related_name='prd_war',on_delete=models.CASCADE)
    product_cost=models.BigIntegerField(default=0)
    stock=models.BigIntegerField(default=0)
    qty=models.BigIntegerField(default=0)
    discount=models.BigIntegerField(default=0)
    tax=models.BigIntegerField(default=0)
    subtotal=models.BigIntegerField(default=0)

class Category(Common):
    category_code=models.IntegerField()
    category_name=models.CharField(max_length=250)
    def __str__(self):
        return str(self.category_name)

class Brand(Common):
    brand_name=models.CharField(max_length=120)
    brand_description=models.CharField(max_length=220)
    brand_image=models.TextField()
    def __str__(self):
        return str(self.brand_name)
class Unit(Common):
    unit_name=models.CharField(max_length=210)
    short_name=models.CharField(max_length=120)
    base_unit=models.CharField(max_length=120,blank=True)
    operator=models.CharField(max_length=10,blank=True)
    operation_value=models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return str(self.unit_name)





















# class userprofile(models.model):

#     address = models.CharField('address', max_length=10)
#     created_user = models.ForeignKey(User, on_delete=models.PROTECT,
#     related_name="userpro_created_user")
#     display_name = models.CharField('display_name', max_length=20)
#     mobile_no = models.IntegerField()
#     role = models.CharField('role', max_length=16)
#     access_roles = models.JSONField('access_roles', blank=False)
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_of_userprofile")
