import pytest
from app.app import app as instance

@pytest.fixture()
def app():
    app = instance
    app.config.update({
        "TESTING": True,
    })

    yield app



@pytest.fixture()
def client(app):
    return app.test_client()
