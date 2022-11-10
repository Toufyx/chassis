"""
created by: {{cookiecutter.author}}
created at: {{cookiecutter.date_creation}}
license: {{cookiecutter.license}}

{{cookiecutter.package}} application factory
"""

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException

from {{cookiecutter.package}}.application.api.exception_handlers import exception_handler
from {{cookiecutter.package}}.application.api.resources import health


def create_app() -> FastAPI:
    """create a fastapi application"""
    app = FastAPI(openapi_url="")

    # routers to expose endpoints
    for resource in (health,):
        app.include_router(resource.router)

    # exception handlers to manage errors
    # custom exception are handled by the generic exception handler
    for exception in (
        HTTPException,
        Exception,
        RequestValidationError,
    ):
        app.add_exception_handler(exception, exception_handler)

    # cors configuration
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
