from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ProductTableSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import ProductTable
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import viewsets

# Create your views here.

class ProductsAPI(APIView):
    def post(self, request):
        serializer = ProductTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Product created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, id=None):
        try:
            if id == None:
                products = ProductTable.objects.all()
                serializer = ProductTableSerializer(products, many=True)
                return Response({"data": serializer.data}, status=status.HTTP_200_OK)
            else:
                product = ProductTable.objects.get(id=id)
                serializer = ProductTableSerializer(product)
                return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, id):
        try:
            if id:
                product = ProductTable.objects.get(id=id)
                serializer = ProductTableSerializer(product, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                return Response({"message":"Product updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Product ID is required for update"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        try:
            if id:
                product = ProductTable.objects.get(id=id)
                product.delete()
                return Response({"message":"Product deleted successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(["POST","GET","PUT","DELETE"])
def ProductAPI(request,product_id=None):
    if request.method == "POST":
        serializer = ProductTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Product created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "GET":
        try:
            if id == None:
                products = ProductTable.objects.all()
                serializer = ProductTableSerializer(products, many=True)
                return Response({"data": serializer.data}, status=status.HTTP_200_OK)
            else:
                product = ProductTable.objects.get(id=product_id)
                serializer = ProductTableSerializer(product)
                return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "PUT":
        try:
            if id:
                product = ProductTable.objects.get(id=product_id)
                serializer = ProductTableSerializer(product, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                return Response({"message":"Product updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Product ID is required for update"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        
class ProductListCreate(generics.ListCreateAPIView):
    queryset = ProductTable.objects.all()
    serializer_class = ProductTableSerializer
    
class ProductUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductTable.objects.all()
    serializer_class = ProductTableSerializer
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductTable.objects.all()
    serializer_class = ProductTableSerializer