from django.contrib import admin
from django.contrib.admin import register

from .models import (Restaurant, RestaurantImage, RestaurantType, RestaurantUniqueFeature, RestaurantCommonFeature,
                     RestaurantInternationalFoodType, RestaurantMainFoodType)


# Register your models here.
@register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'name', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('restaurant', 'name')
    list_editable = ('is_active',)
    list_filter = ('restaurant', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'restaurant__username', 'mobile_number')


@register(RestaurantImage)
class RestaurantImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'image', 'created_at', 'updated_at')
    list_display_links = ('restaurant',)
    list_filter = ('restaurant', 'created_at', 'updated_at')
    search_fields = ('restaurant__name',)


@register(RestaurantType)
class RestaurantTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'type', 'created_at', 'updated_at')
    list_display_links = ('restaurant',)
    list_filter = ('restaurant', 'type', 'created_at', 'updated_at')
    search_fields = ('restaurant__name', 'type__type')


@register(RestaurantUniqueFeature)
class RestaurantUniqueFeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'unique_feature', 'created_at', 'updated_at')
    list_display_links = ('restaurant',)
    list_filter = ('restaurant', 'unique_feature', 'created_at', 'updated_at')
    search_fields = ('restaurant__name', 'unique_feature__unique_feature_name')


@register(RestaurantCommonFeature)
class RestaurantCommonFeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'common_feature', 'created_at', 'updated_at')
    list_display_links = ('restaurant',)
    list_filter = ('restaurant', 'common_feature', 'created_at', 'updated_at')
    search_fields = ('restaurant__name', 'common_feature__common_feature_name')


@register(RestaurantInternationalFoodType)
class RestaurantInternationalFoodTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'international_food_type', 'created_at', 'updated_at')
    list_display_links = ('restaurant',)
    list_filter = ('restaurant', 'international_food_type', 'created_at', 'updated_at')
    search_fields = ('restaurant__name', 'international_food_type__international_type')


@register(RestaurantMainFoodType)
class RestaurantMainFoodTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'main_food_type', 'created_at', 'updated_at')
    list_display_links = ('restaurant',)
    list_filter = ('restaurant', 'main_food_type', 'created_at', 'updated_at')
    search_fields = ('restaurant__name', 'main_food_type__main_type')
