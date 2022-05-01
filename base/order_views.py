from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status
from .serializers import (
    ProductSerializer,
    UserSerializer,
    UserSerializerWithToken,
    OrderSerializer,
)
from .models import Product, Order, ShippingAddress, OrderItem
from rest_framework import status
from datetime import datetime


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_order_items(request):
    user = request.user
    data = request.data
    orderItems = data["orderItems"]
    if orderItems and len(orderItems) == 0:
        return Response(
            {"detail": "No order items"}, status=status.HTTP_400_BAD_REQUEST
        )

    order = Order.objects.create(
        user=user,
        paymentMethod=data["paymentMethod"],
        taxPrice=data["taxPrice"],
        shippingPrice=data["shippingPrice"],
        totalPrice=data["totalPrice"],
    )

    shipping = ShippingAddress.objects.create(
        order=order,
        address=data["shippingAddress"]["address"],
        city=data["shippingAddress"]["city"],
        postalCode=data["shippingAddress"]["postalCode"],
        country=data["shippingAddress"]["country"],
    )

    for i in orderItems:
        product = Product.objects.get(_id=i["product"])
        item = OrderItem.objects.create(
            product=product,
            order=order,
            name=product.name,
            qty=i["qty"],
            price=i["price"],
            image=product.image.url,
        )
        product.countInStock -= item.qty
        product.save()
    serializer = OrderSerializer(order, many=False)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_order_by_id(request, pk):
    user = request.user
    try:
        order = Order.objects.get(_id=pk)
        if user.is_staff or order.user == user:
            serializer = OrderSerializer(order, many=False)

            return Response(serializer.data)

        return Response(
            {"detail": "Not authorized to view this order"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    except:
        return Response(
            {"detail": "Order does not exits"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_order_to_paid(request, pk):
    order = Order.objects.get(_id=pk)
    order.isPaid = True
    order.paidAt = datetime.now()
    order.save()
    return Response("Order was paid", status=status.HTTP_200_OK)
