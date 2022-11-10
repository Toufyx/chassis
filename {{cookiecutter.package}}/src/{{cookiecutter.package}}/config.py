"""
created by: {{cookiecutter.author}}
created at: {{cookiecutter.date_creation}}
licene: {{cookiecutter.license}}

{{cookiecutter.package}} configuration
"""

from os import getenv


def get_string(key: str, default: str) -> str:
    """return string value from env variables"""
    return getenv(key, default)


# general config
SERVICE = get_string("SERVICE", "{{cookiecutter.package}}")
VERSION = get_string("VERSION", "dev")

# identifier generation configuration
IDENTIFIER_ALPHABET = "abcdefghijklmnopqrstuvxyz"
IDENTIFIER_SIZE = 8
