from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import RequestOTPView, VerifyOTPView, CurrentUserView, LogOutView

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
    path(
        'me/',
        CurrentUserView.as_view(),
        name='current-user'
    ),
    path(
        'logout/',
        LogOutView.as_view(),
        name='logout'
    ),
    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token-refresh'
    )

]
