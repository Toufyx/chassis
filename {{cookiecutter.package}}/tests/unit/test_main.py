"""
created by: {{cookiecutter.author}}
created at: {{cookiecutter.date_creation}}
licene: {{cookiecutter.license}}

unit testing {{cookiecutter.package}} applications' entrypoint
"""

from fastapi import FastAPI
from starlette.exceptions import HTTPException

from {{cookiecutter.package}}.main import app


def test_app():
    """test app creation"""
    resources = [route.path for route in app.router.routes]  # type: ignore

    assert isinstance(app, FastAPI)
    assert Exception in app.exception_handlers
    assert HTTPException in app.exception_handlers
    assert "/openapi.json" not in resources
    assert "/docs" not in resources
    assert "/redoc" not in resources
    assert "/readyz" in resources
    assert "/livez" in resources
