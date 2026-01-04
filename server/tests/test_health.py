import pytest


def test_health_check(client):
    """Test that the health check endpoint returns a successful response"""
    response = client.get("/")
    
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert data["status"] == "healthy"
    assert "message" in data
    assert "Smart Insight Dashboard API" in data["message"]


def test_health_check_structure(client):
    """Test that the health check response has the expected structure"""
    response = client.get("/")
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    # Verify required keys exist and have correct types
    assert "status" in data
    assert "message" in data
    assert isinstance(data["status"], str)
    assert isinstance(data["message"], str)
