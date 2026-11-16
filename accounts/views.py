from django.contrib.auth import logout
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import User
from accounts.serializers import (
    CurrentUserSerializer,
    RequestOTPSerializer,
    VerifyOTPSerializer,
)
from accounts.services.otp_service import request_otp, verify_otp


class RequestOTPView(APIView):
    permission_classes = [AllowAny]

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


class VerifyOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data['phone_number']
        code = serializer.validated_data['code']

        is_valid = verify_otp(phone_number, code)
        if not is_valid:
            return Response(
                data={
                    'detail': 'کد تأیید نامعتبر یا منقضی شده است.'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = User.objects.get(phone_number=phone_number)
            created = False
        except User.DoesNotExist:
            user = User.objects.create_user(
                phone_number=phone_number,
                is_active=True
            )
            created = True

        if not user.is_active:
            return Response(
                data={
                    'detail': 'حساب کاربری شما غیرفعال است.'
                },
                status=status.HTTP_403_FORBIDDEN
            )
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                'detail': 'شماره موبایل با موفقیت تأیید شد.',
                'is_new_user': created,
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            },
            status=status.HTTP_200_OK
        )


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CurrentUserSerializer(request.user)
        return Response(serializer.data)


class LogOutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)

        return Response(
            {'detail': 'با موفقیت از حساب کاربری خارج شدید.'},
            status=status.HTTP_200_OK
        )
