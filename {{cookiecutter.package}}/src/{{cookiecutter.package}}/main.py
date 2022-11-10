"""
created by: {{cookiecutter.author}}
created at: {{cookiecutter.date_creation}}
licene: {{cookiecutter.license}}

{{cookiecutter.package}} applications' entrypoint
"""

from {{cookiecutter.package}}.application.api.app import create_app

app = create_app()
