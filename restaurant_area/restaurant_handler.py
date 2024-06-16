from django.db.utils import IntegrityError

from .models import Restaurant


class RestaurantHandler:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def sign_up(self, restaurant, name, address, mobile_number, landline_number, link, social_media):
        try:
            validation_result, message = self.main_validator(
                name,
                mobile_number,
                landline_number,
                social_media,
            )
            if validation_result:
                Restaurant.objects.create(
                    restaurant=restaurant,
                    name=name,
                    address=address,
                    mobile_number=mobile_number,
                    landline_number=landline_number,
                    link=link,
                    social_media=social_media,
                )

                message = "Restaurant created successfully"

            return message

        except IntegrityError:
            return "Restaurant with this name already exists"

    def main_validator(self, name, mobile_number, landline_number, social_media):
        if len(name) > 50:
            return False, "Maximum character length for name is 50"

        if len(mobile_number) != 11:
            return False, "A mobile number should be 11 digits long"

        if mobile_number[0] != '0' or mobile_number[1] != '9':
            return False, "Your mobile number should start width 09"

        for item in mobile_number:
            if not item.isdigit():
                return False, "Please enter your mobile number correctly"

        if len(landline_number) != 8:
            return False, "A landline number should be 8 digits long(do not enter your city code)"

        for item in landline_number:
            if not item.isdigit():
                return False, "Please enter your landline number correctly"

        correct_social_media = ['Instagram', 'Telegram', 'Twitter']

        if social_media not in correct_social_media:
            return False, "Please choose one of the options"

        return True, ""
