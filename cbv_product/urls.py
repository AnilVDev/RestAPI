from django.urls import path,include
from .views import FetchAndSave, ProductView, ProductDetailView


urlpatterns = [
    path('fetch-products/', FetchAndSave.as_view(), name='fetch_products'),
    path('products/', ProductView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail')
]