from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('products/', views.getRoutes, name='products'),
    path('product/<str:pk>', views.getRoutes, name='product')
    
]

