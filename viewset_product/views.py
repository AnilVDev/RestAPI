from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets 
import requests
from product.models import Product 
from .serializers import ViewsetProductSerializer 


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ViewsetProductSerializer

    def fetch_and_save_data(self, request):
        respose = requests.get('https://api.restful-api.dev/objects')

        if response.status_code == 200:
            products = response.json()

            for product in products:
                data = product.get('data', {})
                # Normalize the data keys to lower case
                if data:
                    normalized_data = {k.lower(): v for k, v in data.items()}
                else:
                    normalized_data = {}

                # Update or create Product in the database
                Product.objects.update_or_create(
                    name=product['name'],
                    defaults={
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

            return Response({'message': "Data fetched and saved successfully"}, status=status.HTTP_200_OK)

        else:
            return Response({'error': "Failed to fetch data"}, status=status.HTTP_400_BAD_REQUEST)        