from rest_framework import serializers
from apps.audit.infrastructure.django_models import AuditLog

class AuditLogSerializer(serializers.ModelSerializer):
    user_phone = serializers.CharField(source='user.phone', read_only=True)
    
    class Meta:
        model = AuditLog
        fields = ['id', 'user', 'user_phone', 'action', 'metadata', 'ip_address', 'created_at']
        read_only_fields = ['id', 'created_at']
