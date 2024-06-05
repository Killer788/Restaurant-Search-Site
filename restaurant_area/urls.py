from django.urls import path, include
from rest_framework import routers

from .views import RestaurantsViewSet


restaurants_router = routers.DefaultRouter()
restaurants_router.register('', RestaurantsViewSet)

urlpatterns = [
    path('restaurants/', include(restaurants_router.urls)),
]
