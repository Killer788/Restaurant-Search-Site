from django.db import models


# Create your models here.
class TypeOfRestaurant(models.Model):
    type = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name='Type',
        unique=True,
    )

    class Meta:
        verbose_name = 'Type of Restaurant'
        verbose_name_plural = 'Type of Restaurants'
        ordering = ('pk',)

    def __str__(self):
        return self.type


class UniqueFeature(models.Model):
    unique_feature_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name='Unique Feature Name',
        unique=True,
    )

    class Meta:
        verbose_name = 'Unique Feature'
        verbose_name_plural = 'Unique Features'
        ordering = ('pk',)

    def __str__(self):
        return self.unique_feature_name


class CommonFeature(models.Model):
    common_feature_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name='Common Feature Name',
        unique=True,
    )

    class Meta:
        verbose_name = 'Common Feature'
        verbose_name_plural = 'Common Features'
        ordering = ('pk',)

    def __str__(self):
        return self.common_feature_name


class InternationalFoodType(models.Model):
    international_type = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name='International Type',
        unique=True,
    )

    class Meta:
        verbose_name = 'International Food Type'
        verbose_name_plural = 'International Food Types'
        ordering = ('pk',)

    def __str__(self):
        return self.international_type


class MainFoodType(models.Model):
    main_type = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name='Main Type',
        unique=True,
    )

    class Meta:
        verbose_name = 'Main Food Type'
        verbose_name_plural = 'Main Food Types'
        ordering = ('pk',)

    def __str__(self):
        return self.main_type
