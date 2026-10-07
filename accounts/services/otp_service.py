import secrets
from datetime import timedelta

from django.contrib.auth.hashers import make_password
from django.utils import timezone

from accounts.models import PhoneOTP


def generate_otp():
    return ''.join(
        str(secrets.randbelow(10))
        for _ in range(6)
    )


def request_otp(phone_number):
    otp = generate_otp()

    code_hash = make_password(otp)

    expires_at = timezone.now() + timedelta(minutes=2)

    PhoneOTP.objects.filter(
        phone_number=phone_number,
        is_used=False,
    ).update(
        is_used=True
    )

    PhoneOTP.objects.create(
        phone_number=phone_number,
        code_hash=code_hash,
        expires_at=expires_at,
    )

    return otp
