from rest_framework import serializers


class RequestOTPSerializer(serializers.Serializer):
    phone_number = serializers.RegexField(
        regex=r'^09[0-9]{9}$',
        error_messages={
            'invalid': 'شماره موبایل باید 11 رقم باشد و با 09 شروع شود.'
        }
    )
