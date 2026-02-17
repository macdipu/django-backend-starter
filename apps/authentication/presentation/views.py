from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import PhonePinTokenSerializer

class PhonePinLoginView(TokenObtainPairView):
    serializer_class = PhonePinTokenSerializer
