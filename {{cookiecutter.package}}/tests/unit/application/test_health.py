"""
created by: {{cookiecutter.author}}
created at: {{cookiecutter.date_creation}}
license: {{cookiecutter.license}}

unit testing {{cookiecutter.package}} health indicators
"""

from datetime import datetime
from datetime import timezone
from unittest.mock import Mock
from unittest.mock import patch

from {{cookiecutter.package}}.application.health import ApplicationReadiness
from {{cookiecutter.package}}.application.health import Check
from {{cookiecutter.package}}.application.health import Status

NOW = datetime(2020, 1, 1, tzinfo=timezone.utc)


def mock_datetime(now: datetime) -> Mock:
    """mock the datetime module and setup a now return value"""
    mock = Mock()
    mock.now.return_value = now
    return mock


def test_status_all():
    """test the all class method"""
    assert Status.all([Status.PASS, Status.PASS]) == Status.PASS
    assert Status.all([Status.PASS, Status.FAIL]) == Status.FAIL
    assert Status.all([Status.FAIL, Status.PASS]) == Status.FAIL
    assert Status.all([Status.FAIL, Status.FAIL]) == Status.FAIL


@patch("{{cookiecutter.package}}.application.health.datetime", new=mock_datetime(now=NOW))
def test_application_readiness():
    """test application readiness health indicator"""
    assert ApplicationReadiness().get_check() == Check(
        name="{{cookiecutter.package}}:ready",
        time=NOW,
        status=Status.PASS,
        observed_value="true",
        observed_unit="boolean",
    )
