"""Desarrollo local."""

import os

os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("SECRET_KEY", "solo-para-desarrollo-local")
os.environ.setdefault("ALLOWED_HOSTS", "localhost,127.0.0.1,.trycloudflare.com")
os.environ.setdefault("CSRF_TRUSTED_ORIGINS", "https://*.trycloudflare.com")
os.environ.setdefault("DATABASE_URL", "postgres:///todocargo")

from .base import *  # noqa: E402, F403

# En desarrollo los estáticos se sirven sin manifiesto (no requiere collectstatic).
STORAGES["staticfiles"] = {  # noqa: F405
    "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"
}
