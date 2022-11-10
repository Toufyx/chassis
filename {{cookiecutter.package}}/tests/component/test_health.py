"""
created by: {{cookiecutter.author}}
created at: {{cookiecutter.date_creation}}
license: {{cookiecutter.license}}

testing {{cookiecutter.package}} health resources behaviour
"""

import requests

from tests.utils import AnyDatetimeString
from tests.utils import AnyInstanceOf


def test_livez(host, port):
    """test the /livez endpoint"""
    url = f"http://{host}:{port}/livez"

    response = requests.get(url, timeout=1)

    assert response.status_code == 200
    assert response.json() == {
        "checks": [
            {
                "name": "{{cookiecutter.package}}:ready",
                "observedUnit": "boolean",
                "observedValue": "true",
                "status": "pass",
                "time": AnyDatetimeString(),
            },
        ],
        "service": "{{cookiecutter.package}}",
        "status": "pass",
        "version": AnyInstanceOf(str),
    }


def test_readyz(host, port):
    """test the /readyz endpoint"""
    url = f"http://{host}:{port}/readyz"

    response = requests.get(url, timeout=1)

    assert response.status_code == 200
    assert response.json() == {
        "checks": [
            {
                "name": "{{cookiecutter.package}}:ready",
                "observedUnit": "boolean",
                "observedValue": "true",
                "status": "pass",
                "time": AnyDatetimeString(),
            }
        ],
        "service": "{{cookiecutter.package}}",
        "status": "pass",
        "version": AnyInstanceOf(str),
    }
