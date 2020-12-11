from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('create_product/', views.createProduct, name='create_product'),
    path('update_product/<str:pk>', views.updateProduct, name='update_product'),
    path('delete_product/<str:pk>', views.deleteProduct, name='delete_product'),
    path('custumer/<str:pk>', views.custumer, name='custumer'),
    path('create_order/', views.createOrder, name='create_order'),
    path('update_order/<str:pk>', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>', views.deleteOrder, name='delete_order'),
]

