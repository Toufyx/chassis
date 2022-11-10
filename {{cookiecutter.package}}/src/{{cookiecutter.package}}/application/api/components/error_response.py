"""
created by: {{cookiecutter.author}}
created at: {{cookiecutter.date_creation}}
license: {{cookiecutter.license}}

{{cookiecutter.package}} api error response
"""

from typing import Any
from typing import Optional

from {{cookiecutter.package}}.application.api.components.base import APIComponent


class ErrorResponse(APIComponent):
    """API component representing any error"""

    code: str
    data: Optional[Any] = None
    message: str
