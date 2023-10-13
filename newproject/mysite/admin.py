from django.contrib import admin

# Register your models here.
from mysite.models import Product,Customer,ProdCategory,Order,CustEnq,EnquiryCat,LoginDetails
admin.site.register(ProdCategory)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(EnquiryCat)
admin.site.register(CustEnq)
admin.site.register(LoginDetails)