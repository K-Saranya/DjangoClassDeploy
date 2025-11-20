from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("products-viewset",ProductViewSet)


urlpatterns = [
    path('products', ProductsAPI.as_view()),
    path('products/<int:id>', ProductsAPI.as_view()),
    path('product-api/', ProductAPI),
    path('product-api/<int:product_id>', ProductAPI),
    path('products-generic/', ProductListCreate.as_view()),
    path('products-generic/<int:pk>', ProductUpdate.as_view()),
    path('',include(router.urls))
]
