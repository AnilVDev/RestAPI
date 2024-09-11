from django.contrib import admin
from .models import Product
# Register your models here.

class adminProduct(admin.ModelAdmin):
    list_display = (
        'name',               # Name of the product
        'color',              # Color of the product
        'capacity',           # Capacity of the product
        'price',              # Price of the product
        'generation',         # Generation of the product
        'year',               # Year of manufacture
        'cpu_model',          # CPU model of the product
        'hard_disk_size',     # Hard disk size
        'strap_color',        # Strap color of the product
        'case_size',          # Case size of the product
        'description',        # Description of the product
    )
    
    # Fields to include in the search bar
    search_fields = (
        'name',               # Search by product name
        'color',              # Search by color
        'capacity',           # Search by capacity
        'description',        # Search by description
    )
    
    # Fields to filter by in the sidebar
    list_filter = (
        'color',              # Filter by color
        'price',              # Filter by price
        'generation',         # Filter by generation
        'year',               # Filter by year
        'cpu_model',          # Filter by CPU model
        'hard_disk_size',     # Filter by hard disk size
    )
    
    # Options for pagination
    list_per_page = 20  
admin.site.register(Product,adminProduct)
