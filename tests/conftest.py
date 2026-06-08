from fastapi.testclient import TestClient
import pytest
from copy import deepcopy

from src.app import app, activities


@pytest.fixture
def client():
    """Provide a TestClient and reset the in-memory `activities` after each test."""
    original = deepcopy(activities)
    client = TestClient(app)
    yield client
    activities.clear()
    activities.update(original)
