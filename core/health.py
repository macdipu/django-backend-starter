from django.db import connection
from django.http import JsonResponse
import redis
import os

def health_check(request):
    return JsonResponse({"status": "ok"})

def db_health_check(request):
    try:
        connection.ensure_connection()
        return JsonResponse({"database": "ok"})
    except Exception:
        return JsonResponse({"database": "error"}, status=500)

def redis_health_check(request):
    try:
        r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379)
        r.ping()
        return JsonResponse({"redis": "ok"})
    except Exception:
        return JsonResponse({"redis": "error"}, status=500)
