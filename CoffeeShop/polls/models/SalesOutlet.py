from django.db import models


class SalesOutlet(models.Model):
    sales_outlet_id = models.AutoField(primary_key=True)
    sales_outlet_type = models.CharField(max_length=20)
    store_square_feet = models.IntegerField()
    store_address = models.CharField(max_length=150)
    store_city = models.CharField(max_length=50)
    store_state_province = models.CharField(max_length=2)
    store_telephone = models.CharField(max_length=15)
    store_postal_code = models.CharField(max_length=10)
    store_longitude = models.DecimalField
    store_latitude = models.DecimalField