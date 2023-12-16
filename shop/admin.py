from django.contrib import admin
# after run manage.py createsuperuser to create a admin pannel to see database
# Register your models here.
from .models import product ,Contact ,Orders ,OrderUpdate# import product from models.py
admin.site.register(product)   # use the keyword to register product model in database
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)