from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render


def inicio(request):
    return render(request, "inicio.html")


def salud(request):
    """Chequeo de salud para la plataforma de despliegue: app viva y base de datos accesible."""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
    except Exception:
        return JsonResponse({"estado": "error", "base_de_datos": False}, status=503)
    return JsonResponse({"estado": "ok", "base_de_datos": True})
