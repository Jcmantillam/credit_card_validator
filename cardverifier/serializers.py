import string
from rest_framework import serializers


class VerifyCardSerializer(serializers.Serializer):
    card_number = serializers.CharField(trim_whitespace=False)

    def validate(self, data):
        digits =  data['card_number'].replace(" ", "")
        for digit in digits:
            if digit not in string.digits:
                error = '\'' + digit + '\'' + " is not a digit."
                raise serializers.ValidationError(
                    {"not_digit": error}
                )

        return data
