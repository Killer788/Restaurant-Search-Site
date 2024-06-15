from .models import Restaurant


class RestaurantHandler:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def sign_up(self, restaurant, name, address, mobile_number, landline_number, link, social_media):
        Restaurant.objects.create(
            restaurant=restaurant,
            name=name,
            address=address,
            mobile_number=mobile_number,
            landline_number=landline_number,
            link=link,
            social_media=social_media,
        )
