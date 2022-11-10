"""
created by: {{cookiecutter.author}}
created at: {{cookiecutter.date_creation}}
license: {{cookiecutter.license}}

unit testing {{cookiecutter.package}} health resources
"""

import json
from datetime import datetime
from unittest.mock import Mock

import pytest

from {{cookiecutter.package}}.application.api.resources.health import get_application_readiness
from {{cookiecutter.package}}.application.api.resources.health import get_livez
from {{cookiecutter.package}}.application.api.resources.health import get_readyz
from {{cookiecutter.package}}.application.health import ApplicationReadiness
from {{cookiecutter.package}}.application.health import Check
from {{cookiecutter.package}}.application.health import Status
from tests.utils import AnyInstanceOf


def mock_request(url: str) -> Mock:
    """create a mock request"""
    mock = Mock()
    mock.url.path = url
    return mock


def mock_health_provider(success: bool = True) -> Mock:
    """create a health provider mock"""
    mock = Mock()
    mock.get_check.return_value = Check(
        name="test",
        time=datetime(2020, 1, 1),
        status=Status.PASS if success else Status.FAIL,
        observed_value="true" if success else "false",
        observed_unit="boolean",
    )
    return mock


def test_get_application_readiness():
    """make sure get_application_readiness returns a ApplicationReadiness"""
    indicator = get_application_readiness()
    assert isinstance(indicator, ApplicationReadiness)


@pytest.mark.asyncio
async def test_readyz():
    """test readyz resource"""
    health_provider = mock_health_provider()

    response = await get_readyz(application_ready=health_provider)

    assert response.status_code == 200
    assert json.loads(response.body) == {
        "checks": [
            {
                "name": "test",
                "observedUnit": "boolean",
                "observedValue": "true",
                "status": "pass",
                "time": "2020-01-01T00:00:00",
            },
        ],
        "service": "{{cookiecutter.package}}",
        "status": "pass",
        "version": AnyInstanceOf(str),
    }


@pytest.mark.asyncio
async def test_livez():
    """test livez resource"""
    health_provider = mock_health_provider()

    response = await get_livez(application_ready=health_provider)

    assert response.status_code == 200
    assert json.loads(response.body) == {
        "checks": [
            {
                "name": "test",
                "observedUnit": "boolean",
                "observedValue": "true",
                "status": "pass",
                "time": "2020-01-01T00:00:00",
            }
        ],
        "service": "{{cookiecutter.package}}",
        "status": "pass",
        "version": AnyInstanceOf(str),
    }
