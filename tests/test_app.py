"""Test Fantastic Brocolli startup."""
from flask import Flask
from src import create_app


def test_create_app() -> None:
    """Test Flask Application Startup."""
    app: Flask = create_app()
    assert isinstance(app, Flask)
