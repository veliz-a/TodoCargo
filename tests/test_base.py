import base64

import pytest


@pytest.mark.django_db
def test_salud_responde_ok(client):
    respuesta = client.get("/salud/")
    assert respuesta.status_code == 200
    assert respuesta.json() == {"estado": "ok", "base_de_datos": True}


@pytest.mark.django_db
def test_inicio_se_muestra(client):
    assert client.get("/").status_code == 200


def _basic(clave):
    return "Basic " + base64.b64encode(f"probador:{clave}".encode()).decode()


@pytest.mark.django_db
def test_clave_acceso_restringe(client, settings):
    settings.CLAVE_ACCESO = "secreta"
    assert client.get("/").status_code == 401
    assert client.get("/", HTTP_AUTHORIZATION=_basic("mala")).status_code == 401
    assert client.get("/", HTTP_AUTHORIZATION=_basic("secreta")).status_code == 200
    assert client.get("/salud/").status_code == 200
