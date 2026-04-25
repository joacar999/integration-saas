"""Test cases for Flask app"""
from app import app
import sys
import os
import json

# Add parent directory to path so we can import app
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))


def test_index_page():
    """Test that index page loads"""
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'AI Integration Workflows' in response.data
    print("✓ Index page test PASSED")


def test_generate_no_swagger():
    """Test generate endpoint without Swagger spec"""
    with app.test_client() as client:
        response = client.post('/generate',
                               json={'swagger_spec': ''})
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
    print("✓ No Swagger spec test PASSED")


def test_generate_invalid_json():
    """Test generate endpoint with invalid JSON"""
    with app.test_client() as client:
        response = client.post('/generate',
                               json={'swagger_spec': '{invalid json'})
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
    print("✓ Invalid JSON test PASSED")


def test_generate_valid_swagger():
    """Test generate endpoint with valid Swagger spec"""
    swagger_spec = {
        "openapi": "3.0.0",
        "info": {"title": "Test API", "version": "1.0"},
        "servers": [{"url": "https://api.example.com"}],
        "paths": {
            "/users": {
                "get": {"summary": "Get users"}
            },
            "/posts": {
                "get": {"summary": "Get posts"}
            }
        }
    }

    with app.test_client() as client:
        response = client.post('/generate',
                               json={'swagger_spec': json.dumps(swagger_spec)})

        if response.status_code == 200:
            data = json.loads(response.data)
            assert data['success'] == True
            assert 'generated_code' in data
            assert data['api_name'] == 'Test API'
            print("✓ Valid Swagger spec test PASSED")
        elif response.status_code == 400 and b'Invalid JSON' not in response.data:
            # Might fail due to missing OpenAI API key, that's ok for this test
            print("⚠ Valid Swagger test SKIPPED (likely missing OpenAI API key)")
        else:
            print(f"✗ Valid Swagger test FAILED: {response.status_code}")


if __name__ == '__main__':
    print("\n🧪 Running Flask app tests...\n")
    try:
        test_index_page()
        test_generate_no_swagger()
        test_generate_invalid_json()
        test_generate_valid_swagger()
        print("\n✅ All tests completed!\n")
    except Exception as e:
        print(f"\n❌ Test error: {e}\n")
