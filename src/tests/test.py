import os

import requests


def test_server_health():
    response = requests.get(
        f"http://127.0.0.1:{os.getenv('DJANGO_EXPOSE_PORT')}/health"
    )
    assert response.status_code == 200
