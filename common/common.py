from django.db import models


class Common(models.Model):
    
    active = models.BooleanField('active', default=True)
    created_date = models.DateTimeField('created_date', auto_now_add=True)
    update_date = models.DateTimeField('update_date', auto_now=True)

    class Meta:
        abstract = True
