import secrets
from datetime import timedelta

from django.contrib.auth.hashers import check_password, make_password
from django.utils import timezone

from accounts.models import PhoneOTP
from accounts.services.sms_service import send_otp_sms


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

    send_otp_sms(phone_number, otp)


MAX_OTP_ATTEMPTS = 3


def verify_otp(phone_number, code):
    otp_record = PhoneOTP.objects.filter(
        phone_number=phone_number,
        is_used=False,
    ).order_by('-created_at').first()

    if otp_record is None:
        return False

    if otp_record.expires_at <= timezone.now():
        otp_record.is_used = True
        otp_record.save(update_fields=['is_used'])
        return False

    if otp_record.attempts >= MAX_OTP_ATTEMPTS:
        otp_record.is_used = True
        otp_record.save(update_fields=['is_used'])
        return False

    if not check_password(code, otp_record.code_hash):
        otp_record.attempts += 1

        fields_to_update = ['attempts']

        if otp_record.attempts >= MAX_OTP_ATTEMPTS:
            otp_record.is_used = True
            fields_to_update.append('is_used')

        otp_record.save(update_fields=fields_to_update)
        return False

    otp_record.is_used = True
    otp_record.save(update_fields=['is_used'])
    return True
