from django.urls import path
from .presentation.views import PhonePinLoginView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("login/", PhonePinLoginView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
]
