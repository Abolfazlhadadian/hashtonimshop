
def send_otp_sms(phone_number: str, otp: str) -> None:
    message = f'کد تأیید شما در Hashtonim: {otp}'

    print(
        f'{phone_number} {message}'
    )


send_otp_sms('09121234567', '483921')