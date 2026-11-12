from django.urls import path

from .views import RequestOTPView, VerifyOTPView

app_name = 'accounts'

urlpatterns = [
    path(
        'request-otp/',
        RequestOTPView.as_view(),
        name='request-otp'
    ),

    path(
        'verify-otp/',
        VerifyOTPView.as_view(),
        name='verify-otp'
    ),

]
