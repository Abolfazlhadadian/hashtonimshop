from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import RequestOTPSerializer
from accounts.services.otp_service import request_otp


class RequestOTPView(APIView):
    def post(self, request):
        # 1. دریافت داده‌های درخواست و اعتبارسنجی آن‌ها
        serializer = RequestOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 2. گرفتن شماره موبایل اعتبارسنجی‌شده
        phone_number = serializer.validated_data['phone_number']

        # 3. اجرای منطق درخواست OTP
        request_otp(phone_number)

        # 4. ساخت پاسخ HTTP
        return Response(
            data={'detail': 'درخواست کد تأیید با موفقیت پردازش شد.'},
            status=status.HTTP_200_OK
        )
