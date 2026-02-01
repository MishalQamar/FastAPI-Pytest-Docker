import os

import pytest
from fastapi.testclient import TestClient

from app.config import Settings, get_settings
from app import main


def get_settings_override():
    database_url = os.environ.get("DATABASE_TEST_URL") or os.environ.get("DATABASE_URL")
    return Settings(testing=True, database_url=database_url)


@pytest.fixture(scope="module")
def test_app():
    main.app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(main.app) as test_client:
        yield test_client
