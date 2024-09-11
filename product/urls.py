from django.urls import path 
from . import views




urlpatterns = [
    path('fetch-products/',views.fetch_and_save_data, name = 'fetch_products'),
    path('products/', views.product_list, name='product-list'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),
]