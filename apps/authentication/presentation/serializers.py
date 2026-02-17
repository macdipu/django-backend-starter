from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import serializers

class PhonePinTokenSerializer(TokenObtainPairSerializer):
    phone = serializers.CharField()
    pin = serializers.CharField(write_only=True)

    def __init__(self, *args, **kwargs):
        serializers.Serializer.__init__(self, *args, **kwargs)
        self.fields = {
            'phone': serializers.CharField(),
            'pin': serializers.CharField(write_only=True)
        }

    def validate(self, attrs):
        phone = attrs.get("phone")
        pin = attrs.get("pin")

        user = authenticate(
            request=self.context.get("request"),
            phone=phone,
            password=pin
        )

        if not user:
            raise serializers.ValidationError("Invalid phone or PIN")

        # Manually create tokens since we don't use the default validate
        from rest_framework_simplejwt.tokens import RefreshToken
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
