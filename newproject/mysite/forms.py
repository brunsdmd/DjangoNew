from django import forms
from mysite.models import ProdCategory
from mysite.models import Product
from mysite.models import Customer
from mysite.models import Order
from mysite.models import EnquiryCat
from mysite.models import CustEnq
from mysite.models import LoginDetails

# this view is not in use left as an example
#class FormName(forms.Form): #inheritance - forms.Form class gives you standard aesthetic forms you cant exchange data.
#    name = forms.CharField()
#    email = forms.EmailField()
#    text = forms.CharField(widget=forms.Textarea)

class OrderForm(forms.ModelForm): #inheritance
    # replacing this one with OrderForm
    class Meta:
        model = Order
        exclude = ['OrderTotal']
        

class ContactForm(forms.ModelForm): #inheritance
    class Meta:
        model = CustEnq
        fields = '__all__'

class RegisterForm(forms.ModelForm): #inheritance
    class Meta:
        model = Customer
        fields = '__all__'

class LoginForm(forms.ModelForm): #inheritance
    class Meta:
        model = LoginDetails
        fields = '__all__'

