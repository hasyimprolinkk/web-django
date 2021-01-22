from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.core.paginator import Paginator


from .models import *
from .forms import OrderForm, ProductForm
from .filters import OrderFilter

def home(request):
    list_custumer = Custumer.objects.all()
    list_order = Order.objects.all()
    total_orders = list_order.count()
    delivered = list_order.filter(status = 'Delivered').count()
    pending = list_order.filter(status = 'Pending').count()

    context = {
        'judul': 'Halaman Beranda',
        'menu': 'home',
        'custumer':list_custumer,
        'order':list_order,
        'data_total_orders': total_orders,
        'data_delivered' : delivered,
        'data_pending' : pending,
    }
    return render(request, 'data/dashboard.html', context)

def products(request):
    list_product = Product.objects.order_by('-date_created')
    context = {
        'judul': 'Halaman Produk',
        'menu': 'products',
        'product': list_product,
    }
    return render(request, 'data/products.html', context)

def createProduct(request):
    formproduct = ProductForm()
    if request.method == 'POST':
        formsimpan = ProductForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/products')
    context = {
        'judul': 'Form Product',
        'form' : formproduct, 
    }
    return render(request, 'data/order_form.html', context)

def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    formproduct = ProductForm(instance=product)
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formedit = ProductForm(request.POST, instance=product)
        if formedit.is_valid:
            formedit.save()
            return redirect('/products')
    context = {
        'judul': 'Edit Products',
        'form' : formproduct,
    }
    return render(request, 'data/order_form.html', context)

def deleteProduct(request, pk):
    producthapus = Product.objects.get(id=pk)
    if request.method == 'POST':
        producthapus.delete()
        return redirect('/products')
    context = {
        'judul': 'Hapus Data Product',
        'dataproductdelete' : producthapus,
    }
    return render(request, 'data/delete_product.html', context)

def custumer(request,pk):
    detailcustumer = Custumer.objects.get(id=pk)
    order_custumer = detailcustumer.order_set.all()
    total_custumer = order_custumer.count()
    filter_order   = OrderFilter(request.GET, queryset=order_custumer)
    order_custumer = filter_order.qs

    halaman_tampil = Paginator(order_custumer, 2)
    halaman_url    = request.GET.get('halaman',1)
    halaman_order  = halaman_tampil.get_page(halaman_url)

    if halaman_order.has_previous():
        url_previous = f'?halaman={halaman_order.previous_page_number()}'
    else:
        url_previous = ''
    if halaman_order.has_next():
        url_next = f'?halaman={halaman_order.next_page_number()}'
    else:
        url_next = ''

    context = {
        'judul': 'Halaman Konsumen',
        'custumer': detailcustumer,
        # 'data_order_custumer':order_custumer,
        'halaman_order_custumer':halaman_order,
        'data_total_custumer': total_custumer,
        'filter_data_order': filter_order,
        'previous' : url_previous,
        'next' : url_next,
    }
    return render(request, 'data/custumer.html', context)

def createOrder(request):
    formorder = OrderForm()
    if request.method == 'POST':
        formsimpan = OrderForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/')
    context = {
        'judul': 'Form Order',
        'form' : formorder, 
    }
    return render(request, 'data/order_form.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    formorder = OrderForm(instance=order)
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formedit = OrderForm(request.POST, instance=order)
        if formedit.is_valid:
            formedit.save()
            return redirect('/')        
    context = {
        'judul': 'Edit Order',
        'form' : formorder,
    }
    return render(request, 'data/order_form.html', context)

def deleteOrder(request, pk):
    orderhapus = Order.objects.get(id=pk)
    if request.method == 'POST':
        orderhapus.delete()
        return redirect('/')
    context = {
        'judul': 'Hapus Data Order',
        'dataorderdelete' : orderhapus,
    }
    return render(request, 'data/delete_form.html', context)


