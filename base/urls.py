from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('products/', views.getRoutes, name='products'),
    # path('product/<str:pk>', views.getRoutes, name='product')
    
]

