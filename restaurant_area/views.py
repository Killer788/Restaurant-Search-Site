from django.shortcuts import render, redirect
from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .serializers import RestaurantsSerializer
from .models import Restaurant
from .forms import SignUpForm


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


def sign_up_view(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        return redirect('../')
    else:
        form = SignUpForm()
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()

        context = {'form': form}

        return render(request, 'restaurant_area/sign_up_form.html', context)
