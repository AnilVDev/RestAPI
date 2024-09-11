from django.urls import path, include
from .views import FetchAndSaveGenericView, ProductListCreateView, ProductRetrieveUpdateDestroy


urlpatterns = [
    path('fetch-product/', FetchAndSaveGenericView.as_view(), name='fetch-products'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='product_detail')
]