from django.urls import path, include
from rest_framework import routers

from .views import RestaurantsViewSet, sign_up_view, sign_in_view


restaurants_router = routers.DefaultRouter()
restaurants_router.register('', RestaurantsViewSet)

urlpatterns = [
    path('restaurants/', include(restaurants_router.urls)),
    path('signup/', sign_up_view, name='signup'),
    path('signin/', sign_in_view, name='signin'),
]
