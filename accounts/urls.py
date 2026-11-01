from django.urls import path

from .views import RequestOTPView

app_name = 'accounts'

urlpatterns = [
    path(
        'request-otp/',
        RequestOTPView.as_view(),
        name='request-otp'
    )

]
