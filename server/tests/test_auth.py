import pytest


def test_signup_success(client):
    """Test successful user signup"""
    user_data = {
        "username": "newuser",
        "email": "newuser@example.com",
        "password": "password123"
    }
    response = client.post("/auth/signup", json=user_data)
    
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == user_data["username"]
    assert data["email"] == user_data["email"]
    assert "id" in data
    assert "password" not in data
    assert "hashed_password" not in data


def test_signup_duplicate_username(client, test_user):
    """Test signup fails with duplicate username"""
    user_data = {
        "username": test_user["username"],
        "email": "different@example.com",
        "password": "password123"
    }
    response = client.post("/auth/signup", json=user_data)
    
    assert response.status_code == 400
    assert "already registered" in response.json()["detail"].lower()


def test_signup_duplicate_email(client, test_user):
    """Test signup fails with duplicate email"""
    user_data = {
        "username": "differentuser",
        "email": test_user["email"],
        "password": "password123"
    }
    response = client.post("/auth/signup", json=user_data)
    
    assert response.status_code == 400
    assert "already registered" in response.json()["detail"].lower()


def test_login_success(client, test_user):
    """Test successful login with form data"""
    login_data = {
        "username": test_user["email"],  # OAuth2 uses 'username' field
        "password": test_user["password"]
    }
    response = client.post("/auth/login", data=login_data)
    
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    assert isinstance(data["access_token"], str)
    assert len(data["access_token"]) > 0


def test_login_wrong_password(client, test_user):
    """Test login fails with wrong password"""
    login_data = {
        "username": test_user["email"],
        "password": "wrongpassword"
    }
    response = client.post("/auth/login", data=login_data)
    
    assert response.status_code == 401
    assert "Invalid" in response.json()["detail"]


def test_login_nonexistent_user(client):
    """Test login fails for non-existent user"""
    login_data = {
        "username": "nonexistent@example.com",
        "password": "password123"
    }
    response = client.post("/auth/login", data=login_data)
    
    assert response.status_code == 401
    assert "Invalid" in response.json()["detail"]


def test_protected_route_with_valid_token(client, auth_token, test_user):
    """Test accessing protected route with valid token"""
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.get("/data/protected", headers=headers)
    
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert test_user["username"] in data["message"]
    assert test_user["email"] in data["message"]


def test_protected_route_without_token(client):
    """Test accessing protected route without token fails"""
    response = client.get("/data/protected")
    
    assert response.status_code == 401
    assert "detail" in response.json()


def test_protected_route_with_invalid_token(client):
    """Test accessing protected route with invalid token fails"""
    headers = {"Authorization": "Bearer invalid_token"}
    response = client.get("/data/protected")
    
    assert response.status_code == 401
    detail = response.json()["detail"]
    # Can be either "Not authenticated" or "Could not validate credentials"
    assert "authenticated" in detail.lower() or "credentials" in detail.lower()


def test_protected_route_with_malformed_token(client):
    """Test accessing protected route with malformed token fails"""
    headers = {"Authorization": "InvalidFormat"}
    response = client.get("/data/protected")
    
    assert response.status_code == 401
