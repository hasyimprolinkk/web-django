from django import forms
from django.forms import ModelForm
from .models import Order, Product, Custumer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields= ['username','email','password1','password2']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields= '__all__'
        widgets = {
            'custumer': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }
        labels = {
            'custumer': 'Konsumen',
            'product': 'Produk',
            'status': 'Status Order',
        }

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields= '__all__'
        widgets = {
            'description': forms.Textarea()
        }
        labels = {
            'name': 'Nama',
            'price': 'Harga',
            'category': 'Kategori',
            'description': 'Deskripsi',
        }

class CustumerForm(ModelForm):
    class Meta:
        model = Custumer
        fields= '__all__'
        exclude = ['user']
