"""
Pytest configuration and fixtures for tests.
"""
import os

# Set test database URL before any app imports
os.environ["DATABASE_URL"] = "sqlite:///:memory:"
