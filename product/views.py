import requests
from django.http import JsonResponse
from .models import Product

from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework import status 
from .serializers import ProductSerializer





# Create your views here.
def fetch_and_save_data(request):
    response = requests.get('https://api.restful-api.dev/objects')

    if response.status_code == 200:
        products = response.json()

        for product in products:
            data = product.get('data', {})
            if data:
                normalized_data = {k.lower(): v for k, v in data.items()}
            else:
                normalized_data = {}

            Product.objects.update_or_create(
                name = product['name'],
                defaults = {
                    'color': normalized_data.get('color'),
                    'capacity': normalized_data.get('capacity') or normalized_data.get('capacity gb'),
                    'price': normalized_data.get('price'),
                    'generation': normalized_data.get('generation'),
                    'year': normalized_data.get('year'),
                    'cpu_model': normalized_data.get('cpu model'),
                    'hard_disk_size': normalized_data.get('hard disk size'),
                    'strap_color': normalized_data.get('strap colour'),
                    'case_size': normalized_data.get('case size'),
                    'description': normalized_data.get('description')

                }
            )

        return JsonResponse({'message':"Data fetched and saved successfully"}, status = 200)
    else:
        return JsonResponse({'error':"Failed to fetch to fetch data"}, status=400 )



# List and Create Products 
@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer =  ProductSerializer(products, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        # Create a new product
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['PUT', 'GET', 'DELETE'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data) 
    
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        product.delete()
        return Response({'message': 'Product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        
