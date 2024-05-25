from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

from lib.common_base_models import BaseModel, BaseModelWithIsActive


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
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Name')
    address = models.TextField(null=False, blank=False, verbose_name='Address')
    mobile_number = models.CharField(max_length=11, null=False, blank=False, verbose_name='Mobile Number')
    landline_number = models.CharField(max_length=8, null=False, blank=False, verbose_name='Landline Number')
    link = models.TextField(null=False, blank=False, verbose_name='Link')
    social_media = models.CharField(
        max_length=10,
        choices=settings.SOCIAL_MEDIA_CHOICES,
        default='Instagram',
        verbose_name='Social Media',
    )
