"""Acceso restringido por clave compartida para entornos públicos durante el desarrollo."""

import base64
import secrets

from django.conf import settings
from django.http import HttpResponse

RUTAS_LIBRES = ("/salud/",)


class AccesoRestringidoMiddleware:
    """Pide usuario y clave (autenticación HTTP básica) si CLAVE_ACCESO está definida.

    Cualquier usuario sirve; solo se valida la clave. Se reemplaza en la fase 4 por cuentas reales.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        clave = settings.CLAVE_ACCESO
        if not clave or request.path in RUTAS_LIBRES or self._clave_valida(request, clave):
            return self.get_response(request)
        respuesta = HttpResponse("Acceso restringido", status=401)
        respuesta["WWW-Authenticate"] = 'Basic realm="TodoCargo", charset="UTF-8"'
        return respuesta

    @staticmethod
    def _clave_valida(request, clave):
        cabecera = request.META.get("HTTP_AUTHORIZATION", "")
        tipo, _, datos = cabecera.partition(" ")
        if tipo.lower() != "basic":
            return False
        try:
            _, _, recibida = base64.b64decode(datos).decode().partition(":")
        except (ValueError, UnicodeDecodeError):
            return False
        return secrets.compare_digest(recibida, clave)
