"""
API endpoint tests
"""

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_endpoint():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "TRIZ Trade API"
    assert data["version"] == "1.0.0"

def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"

def test_api_info():
    """Test API info endpoint"""
    response = client.get("/api/v1/info")
    assert response.status_code == 200
    data = response.json()
    assert "endpoints" in data
    assert "stocks" in data["endpoints"]

def test_stocks_endpoint():
    """Test stocks list endpoint"""
    response = client.get("/api/v1/stocks/")
    assert response.status_code in [200, 501]  # 501 if not implemented

def test_currencies_endpoint():
    """Test currencies list endpoint"""
    response = client.get("/api/v1/currencies/")
    assert response.status_code in [200, 501]  # 501 if not implemented

def test_data_status():
    """Test data status endpoint"""
    response = client.get("/api/v1/data/status")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data

def test_data_health():
    """Test data health endpoint"""
    response = client.get("/api/v1/data/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "services" in data 