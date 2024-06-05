from rest_framework import serializers

from restaurant_area.models import Restaurant


class RestaurantsSerializer(serializers.ModelSerializer):
    restaurant_images = serializers.StringRelatedField(many=True)
    restaurant_types = serializers.StringRelatedField(many=True)
    restaurant_unique_features = serializers.StringRelatedField(many=True)
    restaurant_common_features = serializers.StringRelatedField(many=True)
    restaurant_international_food_types = serializers.StringRelatedField(many=True)
    restaurant_main_food_types = serializers.StringRelatedField(many=True)

    class Meta:
        model = Restaurant
        fields = (
            'name',
            'address',
            'mobile_number',
            'landline_number',
            'link',
            'social_media',

            # related_fields
            'restaurant_images',
            'restaurant_types',
            'restaurant_unique_features',
            'restaurant_common_features',
            'restaurant_international_food_types',
            'restaurant_main_food_types',
        )
