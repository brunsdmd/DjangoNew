from django.db import models
from datetime import datetime

# Create your models here.

class Customer(models.Model):
    CustomerId = models.AutoField(primary_key=True)
    CustFirstName = models.CharField(max_length=128,null=False)
    CustLastName = models.CharField(max_length=128,null=False)
    CustCellNo  = models.CharField(max_length=20)
    CustEmail  = models.EmailField(unique=True,null=False)
    CustPassword  = models.CharField(max_length=20)
    
 
    def __str__(self):
        return self.CustFirstName

class ProdCategory(models.Model):
    ProdCatId = models.AutoField(primary_key=True)
    ProdCatName = models.CharField(max_length=128,null=False)

    def __str__(self):
        return self.ProdCatName

class Product(models.Model):
    #Charfield is equal to varchar
    ProductId = models.AutoField(primary_key=True)
    ProdCatId = models.ForeignKey(ProdCategory,on_delete = models.CASCADE)
    ProdName = models.CharField(max_length=100,unique=True,null=False)
    ProdDescr = models.CharField(max_length=128,unique=True,null=False)
    ProdQtyAvail = models.IntegerField()
    ProdPrice = models.IntegerField(null=False)
 
    def __str__(self):
        return self.ProdName

class Order(models.Model):
    OrderId = models.AutoField(primary_key=True)
    ProductId = models.ForeignKey(Product,on_delete = models.CASCADE)
    CustomerId = models.ForeignKey(Customer,on_delete = models.CASCADE)
    Qty = models.IntegerField()
    OrderTotal = models.IntegerField()
    OrderDeliveryAddress = models.CharField(max_length=128,null=False)
    def get_default_datetime():
        # Your custom logic to calculate the default date and time
        return datetime.now()
    OrderDate = models.DateTimeField(max_length=20,default=get_default_datetime)
   
    def __str__(self):
        return self.CustFirstName

class EnquiryCat(models.Model):
    EnqCatId = models.AutoField(primary_key=True)
    EnqCatName = models.CharField(max_length=128,null=False)

    def __str__(self):
        return self.EnqCatName

class CustEnq(models.Model):
    #Charfield is equal to varchar
    EnqId = models.AutoField(primary_key=True)
    CustomerId = models.ForeignKey(Customer,on_delete = models.CASCADE)
    EnqCatId = models.ForeignKey(EnquiryCat,on_delete = models.CASCADE)
    EnqComment = models.CharField(max_length=128,null=False)
    def get_default_datetime():
        # Your custom logic to calculate the default date and time
        return datetime.now()
    EnqDate = models.DateTimeField(max_length=20,default=get_default_datetime)

    def __str__(self):
        return self.EnqComment

class LoginDetails(models.Model):
    LoginId = models.AutoField(primary_key=True)
    CustomerId = models.ForeignKey(Customer, on_delete=models.CASCADE)
    LoginEmail = models.EmailField()
    LoginPassword = models.CharField(max_length=20)
    def get_default_datetime():
        # Your custom logic to calculate the default date and time
        return datetime.now()
    LoginDateTime = models.DateTimeField(default=get_default_datetime)
 
    def __str__(self):
        return self.LoginEmail