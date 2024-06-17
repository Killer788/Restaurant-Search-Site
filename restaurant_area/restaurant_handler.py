import re

import restaurant_area.models
from .models import Restaurant


class RestaurantHandler:
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

        return "Restaurant created successfully"

    def main_validator(self, email, username, password1, password2, name, address, mobile_number,
                       landline_number, link, social_media):
        if len(name) > 50:
            return False, "Maximum character length for name is 50"

        try:
            already_existing_name = Restaurant.objects.get(name__iexact=name)
        except restaurant_area.models.Restaurant.DoesNotExist:
            already_existing_name = ''

        if already_existing_name:
            return False, "Restaurant with this name already exists"

        for item in mobile_number:
            if not item.isdigit():
                return False, "Please enter your mobile number correctly"

        if len(mobile_number) != 11:
            return False, "A mobile number should be 11 digits long"

        if mobile_number[0] != '0' or mobile_number[1] != '9':
            return False, "Your mobile number should start width 09"

        for item in landline_number:
            if not item.isdigit():
                return False, "Please enter your landline number correctly"

        if len(landline_number) != 8:
            return False, "A landline number should be 8 digits long(do not enter your city code)"

        regex = ("((http|https)://)(www.)?" +
                 "[a-zA-Z0-9@:%._\\+~#?&//=]" +
                 "{2,256}\\.[a-z]" +
                 "{2,6}\\b([-a-zA-Z0-9@:%" +
                 "._\\+~#?&//=]*)")
        regex_compiled = re.compile(regex)
        if re.search(regex_compiled, link) is None:
            return False, "Invalid Link was entered. Please make sure that your link starts with 'https://'"

        correct_social_media = ['Instagram', 'Telegram', 'Twitter']
        if social_media not in correct_social_media:
            return False, "Please choose one of the options"

        if (email == "" or username == "" or password1 == "" or password2 == "" or name == "" or address == "" or
                mobile_number == "" or landline_number == "" or link == "" or social_media == ""):
            return False, "It doesn't work this way pal:)"

        return True, ""
