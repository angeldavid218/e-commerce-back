from django.urls import path, include
from rest_framework import routers
from . import views, order_views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r"products", views.ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "users/login/", views.MyTokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("users/profile", views.get_user_profile, name="users-profile"),
    path("users/update", views.update_user_profile, name="users-profile-update"),
    path("users/register", views.registerUser, name="register"),
    path("orders/add/", order_views.add_order_items, name="orders-add"),
    path("orders/<str:pk>/", order_views.get_order_by_id, name="user-order"),
    path("orders/<str:pk>/pay/", order_views.update_order_to_paid, name="pay"),
]
