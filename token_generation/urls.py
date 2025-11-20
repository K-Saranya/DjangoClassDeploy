from django.urls import path
from .views import *

urlpatterns = [
    path('token/', UserCreateAPI.as_view()),
    path('user/token/obtain/', UserLoginAPI.as_view()),
    path('external', externalAPI)
    
]
