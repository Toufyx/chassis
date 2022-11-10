"""
created by: {{cookiecutter.author}}
created at: {{cookiecutter.date_creation}}
license: {{cookiecutter.license}}

{{cookiecutter.package}} integration tests configuration
"""

import pytest
from fastapi.testclient import TestClient

from {{cookiecutter.package}}.main import app


@pytest.fixture(name="client", scope="session")
def fixture_client():
    """return a test client"""
    return TestClient(app)
