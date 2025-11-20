from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from django.http import HttpResponse

# Create your views here.

class UserCreateAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            serializer = OtherDetailsSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                refresh = RefreshToken.for_user(user)
                return Response({"data": serializer.data, "refresh":str(refresh), "access": str(refresh.access_token)} ,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        
class UserLoginAPI(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = TokenLoginSerializer
    
    
import requests

def externalAPI(request):
    result = requests.get("https://jsonplaceholder.typicode.com/users")
    if result.status_code == 200:
        response = result.json()
        print(response)
        return HttpResponse("Hii")
    else:
        print(result.status_code)
        return HttpResponse("Hello")
