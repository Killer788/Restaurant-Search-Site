from django.contrib import admin
from django.contrib.admin import register

from .models import TypeOfRestaurant, UniqueFeature, CommonFeature, InternationalFoodType, MainFoodType


# Register your models here.
@register(TypeOfRestaurant)
class TypeOfRestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')
    list_display_links = ('type',)
    search_fields = ('type',)


@register(UniqueFeature)
class UniqueFeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'unique_feature_name')
    list_display_links = ('unique_feature_name',)
    search_fields = ('unique_feature_name',)


@register(CommonFeature)
class CommonFeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'common_feature_name')
    list_display_links = ('common_feature_name',)
    search_fields = ('common_feature_name',)


@register(InternationalFoodType)
class InternationalFoodTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'international_type')
    list_display_links = ('international_type',)
    search_fields = ('international_type',)


@register(MainFoodType)
class MainFoodTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'main_type')
    list_display_links = ('main_type',)
    search_fields = ('main_type',)
