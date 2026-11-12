from rest_framework import serializers

from accounts.models import User, Profile


class RequestOTPSerializer(serializers.Serializer):
    phone_number = serializers.RegexField(
        regex=r'^09[0-9]{9}$',
        error_messages={
            'invalid': 'شماره موبایل باید 11 رقم باشد و با 09 شروع شود.'
        }
    )


class VerifyOTPSerializer(serializers.Serializer):
    phone_number = serializers.RegexField(
        regex=r'^09[0-9]{9}$',
        error_messages={
            'invalid': 'شماره موبایل باید 11 رقم باشد و با 09 شروع شود.'
        }
    )

    code = serializers.RegexField(
        regex=r'^[0-9]{6}$',
        error_messages={
            'invalid': 'کد تأیید باید دقیقاً 6 رقم باشد.'
        }
    )


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'display_name',
            'biography',
            'avatar',
            'province',
            'city',
            'address',
            'postal_code',
        )


class CurrentUserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'phone_number',
            'email',
            'first_name',
            'last_name',
            'date_joined',
            'profile',
        )
