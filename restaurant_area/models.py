from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

from lib.common_base_models import BaseModel, BaseModelWithIsActive
from types_and_features.models import (TypeOfRestaurant, UniqueFeature, CommonFeature, InternationalFoodType,
                                       MainFoodType)


BaseUser = get_user_model()


# Create your models here.
class Restaurant(BaseModelWithIsActive):
    restaurant = models.ForeignKey(
        BaseUser,
        on_delete=models.CASCADE,
        related_name='restaurants',
        null=False,
        blank=False,
        verbose_name='Restaurant',
    )
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Name', unique=True)
    address = models.TextField(null=False, blank=False, verbose_name='Address')
    mobile_number = models.CharField(max_length=11, null=False, blank=False, verbose_name='Mobile Number')
    landline_number = models.CharField(max_length=8, null=False, blank=False, verbose_name='Landline Number')
    link = models.URLField(null=True, blank=True, verbose_name='Link')
    social_media = models.CharField(
        max_length=10,
        choices=settings.SOCIAL_MEDIA_CHOICES,
        default='Instagram',
        verbose_name='Social Media',
    )

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'
        ordering = ('pk',)

    def __str__(self):
        return self.name


class RestaurantImage(BaseModel):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='restaurant_images',
        null=False,
        blank=False,
        verbose_name='Restaurant',
    )
    image = models.TextField(null=False, blank=False, verbose_name='Image')

    class Meta:
        verbose_name = 'Restaurant Image'
        verbose_name_plural = 'Restaurant Images'
        ordering = ('pk',)

    def __str__(self):
        return self.image


class RestaurantType(BaseModel):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='restaurant_types',
        null=False,
        blank=False,
        verbose_name='Restaurant'
    )
    type = models.ForeignKey(
        TypeOfRestaurant,
        on_delete=models.CASCADE,
        related_name='restaurant_types',
        null=False,
        blank=False,
        verbose_name='Type',
    )

    class Meta:
        verbose_name = 'Restaurant Type'
        verbose_name_plural = 'Restaurant Types'
        ordering = ('pk',)

    def __str__(self):
        return self.type.type


class RestaurantUniqueFeature(BaseModel):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='restaurant_unique_features',
        null=False,
        blank=False,
        verbose_name='Restaurant'
    )
    unique_feature = models.ForeignKey(
        UniqueFeature,
        on_delete=models.CASCADE,
        related_name='restaurant_unique_features',
        null=False,
        blank=False,
        verbose_name='Unique Feature',
    )

    class Meta:
        verbose_name = 'Restaurant Unique Feature'
        verbose_name_plural = 'Restaurant Unique Features'
        ordering = ('pk',)

    def __str__(self):
        return self.unique_feature.unique_feature_name


class RestaurantCommonFeature(BaseModel):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='restaurant_common_features',
        null=False,
        blank=False,
        verbose_name='Restaurant',
    )
    common_feature = models.ForeignKey(
        CommonFeature,
        on_delete=models.CASCADE,
        related_name='restaurant_common_features',
        null=False,
        blank=False,
        verbose_name='Common Feature'
    )

    class Meta:
        verbose_name = 'Restaurant Common Feature'
        verbose_name_plural = 'Restaurant Common Features'
        ordering = ('pk',)

    def __str__(self):
        return self.common_feature.common_feature_name


class RestaurantInternationalFoodType(BaseModel):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='restaurant_international_food_types',
        null=False,
        blank=False,
        verbose_name='Restaurant',
    )
    international_food_type = models.ForeignKey(
        InternationalFoodType,
        on_delete=models.CASCADE,
        related_name='restaurant_international_food_types',
        null=False,
        blank=False,
        verbose_name='International Food Type'
    )

    class Meta:
        verbose_name = 'Restaurant International Food Type'
        verbose_name_plural = 'Restaurant International Food Types'
        ordering = ('pk',)

    def __str__(self):
        return self.international_food_type.international_type


class RestaurantMainFoodType(BaseModel):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='restaurant_main_food_types',
        null=False,
        blank=False,
        verbose_name='Restaurant',
    )
    main_food_type = models.ForeignKey(
        MainFoodType,
        on_delete=models.CASCADE,
        related_name='restaurant_main_food_types',
        null=False,
        blank=False,
        verbose_name='Main Food Type'
    )

    class Meta:
        verbose_name = 'Restaurant Main Food Type'
        verbose_name_plural = 'Restaurant Main Food Types'
        ordering = ('pk',)

    def __str__(self):
        return self.main_food_type.main_type
