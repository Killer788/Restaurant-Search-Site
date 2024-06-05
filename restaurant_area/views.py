from django.shortcuts import render
from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import RestaurantsSerializer
from .models import Restaurant


# Create your views here.
class RestaurantsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RestaurantsSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Restaurant.objects.filter(is_active=True).all()

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    filterset_fields = (
        'restaurant_types',
        'restaurant_unique_features',
        'restaurant_common_features',
        'restaurant_international_food_types',
        'restaurant_main_food_types',
    )
    search_fields = (
        'name',
        'address',
        'mobile_number',
        'landline_number',
    )
