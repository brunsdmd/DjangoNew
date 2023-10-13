from django.shortcuts import render, redirect
from mysite.models import ProdCategory
from mysite.models import Product
from mysite.models import Customer
from mysite.models import EnquiryCat
from mysite.models import CustEnq
from mysite.models import Order
from mysite.models import LoginDetails

from . import forms
from django.http import HttpResponse

# Create your views here.

def about_us(request):
    about_text = "About Our Company"
    return render(request, "mysite/about.html", {'about_text': about_text})

def contact_name_view(request):
    form = forms.ContactForm()
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid:
            form.save(commit=True)
            return index(request)
        else:
            print('Invalid form')
    return render(request, 'mysite/contact.html', {'form':form})

def register_name_view(request):
    form = forms.RegisterForm()
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid:
            form.save(commit=True)
            return index(request)
        else:
            print('Invalid form')
    return render(request, 'mysite/register.html', {'form':form})

def login_name_view(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            # Access the customer instance from the form
            customer_instance = form.cleaned_data['CustomerId']
            
            # Access the related model's field, assuming Password is a field in your Customer model
            Email = customer_instance.CustEmail
            Password = customer_instance.CustPassword

            LoginEmail = form.cleaned_data['LoginEmail']
            LoginPassword = form.cleaned_data['LoginPassword']

            if LoginEmail == Email:
                if LoginPassword == Password:
                    form.save(commit=True)
                    return index(request)
                else:
                    return render(request, 'mysite/profile.html', {'error_message': 'Incorrect password'})
            else:
                return render(request, 'mysite/login.html', {'error_message': 'Incorrect email/username'})
            
        else:
            print('Invalid form')
    return render(request, 'mysite/login.html', {'form':form})

def buy_product_view(request):
    form = forms.OrderForm()
    if request.method == 'POST':
        form = forms.OrderForm(request.POST)
        if form.is_valid():

            # Access the product instance from the form
            product_instance = form.cleaned_data['ProductId']
            
            # Access the related model's field, assuming ProdPrice is a field in your Product model
            ProdPrice = product_instance.ProdPrice

            Qty = form.cleaned_data['Qty']
            OrderTotal = ProdPrice * Qty 
            form.instance.OrderTotal = OrderTotal         

            # Pass order_total to the template
        form.save(commit=True)
 
        # Update Product table
        product_instance.ProdQtyAvail -= Qty
        product_instance.save()
        return index(request)
        return render(request, 'mysite/order.html', {'form': form, 'OrderTotal': OrderTotal})
    else:
            print('Invalid form')
    return render(request, 'mysite/order.html', {'form':form})
   

def index(request):
    customer = Order.objects.all
    my_dict = {'customers' : customer}
    return render(request, "mysite/index.html", context = my_dict)
 
def shopping_detail(request):
    order = Order.objects.all
    my_dict = {'orders' : order}
    return render(request, "mysite/shopping_detail.html", context = my_dict)

def profile(request):
    about_text = "Register or Login"
    return render(request, "mysite/profile.html", {'about_text': about_text})
