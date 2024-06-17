from django.shortcuts import render, redirect
from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .serializers import RestaurantsSerializer
from .models import Restaurant, BaseUser
from .forms import SignUpForm
from .restaurant_handler import RestaurantHandler


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
    message = ''
    if request.user.is_authenticated and not request.user.is_superuser:
        return redirect('../')
    else:
        form = SignUpForm()
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                email = request.POST['email']
                username = request.POST['username']
                password1 = request.POST['password1']
                password2 = request.POST['password2']
                name = request.POST['restaurant_name']
                address = request.POST['address']
                mobile_number = request.POST['mobile_number']
                landline_number = request.POST['landline_number']
                link = request.POST['link']
                social_media = request.POST['social_media']

                restaurant_handler = RestaurantHandler()
                validation_result, message = restaurant_handler.main_validator(
                    email=email,
                    username=username,
                    password1=password1,
                    password2=password2,
                    name=name,
                    address=address,
                    mobile_number=mobile_number,
                    landline_number=landline_number,
                    link=link,
                    social_media=social_media,
                )
                if validation_result:
                    form.save()
                    base_restaurant_instance = BaseUser.objects.get(username=username)
                    message = restaurant_handler.sign_up(
                        restaurant=base_restaurant_instance,
                        name=name,
                        address=address,
                        mobile_number=mobile_number,
                        landline_number=landline_number,
                        link=link,
                        social_media=social_media,
                    )

        context = {'form': form, 'message': message}

        return render(request, 'restaurant_area/sign_up_form.html', context)


def sign_in_view(request):
    message = ''
    if request.user.is_authenticated and not request.user.is_superuser:
        return redirect('../')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            if username == '' or password == '':
                message = 'Please fill out all the required fields'
            else:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('../')
                else:
                    message = 'Username or Password is incorrect'

        context = {'message': message}

        return render(request, '', context)
