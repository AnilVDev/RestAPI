from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from product.models import Product
from .serializers import CbvProductSerializer
import requests


# Create your views here.
class FetchAndSave(APIView):
    def get(self, request):
        response = requests.get('https://api.restful-api.dev/objects')

        if response.status_code == 200:
            products = response.json()

            for product in products:
                data = product.get('data', {})
                if data:
                    normalized_data = {k.lower():v for k,v in data.items()}
                else:
                    normalized_data = {}

                Product.objects.update_or_create(
                    name = product['name'],
                    defaults = {
                        'color':normalized_data.get('color'),
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
            return Response({'message' : "Data fetched and saved successfully"}, status=status.HTTP_200_OK)    

        else:
            return Response({'error': "Failed to fetch data"}, status=status.HTTP_400_BAD_REQUEST)        
        


class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = CbvProductSerializer(products, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CbvProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error':'product not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CbvProductSerializer(product)
        return Response(serializer.data)

    def patch(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error':'product not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CbvProductSerializer(product, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error':'product not found'}, status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response({'message':'profuct deleted successfully'}, status=status.HTTP_204_NO_CONTENT)        
