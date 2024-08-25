from django.contrib import admin
from .models import SalesReceipts, SalesOutlet, Product, Customer

# Register your models here.
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(SalesOutlet)
admin.site.register(SalesReceipts)