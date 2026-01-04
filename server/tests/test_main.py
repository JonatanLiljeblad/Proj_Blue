"""
Tests for the main FastAPI application and health check endpoint.
"""
import pytest
import os
from fastapi.testclient import TestClient

# Set a test database URL before importing the app
os.environ["DATABASE_URL"] = "sqlite:///:memory:"

from app.main import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)


def test_health_check(client):
    """Test that the root endpoint returns a healthy status."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert data["status"] == "healthy"
    assert "message" in data


def test_app_starts_without_error(client):
    """Test that the FastAPI app starts without errors."""
    # This test validates that the app initializes correctly
    # If there's a startup error (like Title vs title), this will fail
    assert client.app is not None
    assert hasattr(client.app, "title")
    assert client.app.title == "Smart Insight Dashboard API"
