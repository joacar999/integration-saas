"""Test Swagger/OpenAPI parsing functionality"""
import json


def parse_swagger_spec(swagger_json_str):
    """Parse and validate Swagger spec"""
    try:
        spec = json.loads(swagger_json_str)
        return {
            'title': spec.get('info', {}).get('title', 'Unknown'),
            'version': spec.get('info', {}).get('version', 'Unknown'),
            'base_url': spec.get('servers', [{}])[0].get('url', 'N/A'),
            'endpoints': list(spec.get('paths', {}).keys()),
            'endpoint_count': len(spec.get('paths', {}))
        }
    except json.JSONDecodeError as e:
        return {'error': f'Invalid JSON: {str(e)}'}


def test_valid_swagger():
    """Test parsing valid Swagger spec"""
    swagger = {
        "openapi": "3.0.0",
        "info": {
            "title": "Pet Store API",
            "version": "1.0.0"
        },
        "servers": [
            {"url": "https://petstore.api.com"}
        ],
        "paths": {
            "/pets": {"get": {}, "post": {}},
            "/pets/{id}": {"get": {}, "delete": {}}
        }
    }

    result = parse_swagger_spec(json.dumps(swagger))
    assert result['title'] == 'Pet Store API'
    assert result['base_url'] == 'https://petstore.api.com'
    assert result['endpoint_count'] == 2
    print("✓ Valid Swagger parsing test PASSED")


def test_swagger_without_servers():
    """Test Swagger without servers field"""
    swagger = {
        "openapi": "3.0.0",
        "info": {"title": "My API", "version": "2.0"},
        "paths": {
            "/users": {"get": {}}
        }
    }

    result = parse_swagger_spec(json.dumps(swagger))
    assert result['title'] == 'My API'
    assert result['base_url'] == 'N/A'
    assert result['endpoint_count'] == 1
    print("✓ Swagger without servers test PASSED")


def test_invalid_json():
    """Test parsing invalid JSON"""
    result = parse_swagger_spec("{not valid json}")
    assert 'error' in result
    print("✓ Invalid JSON test PASSED")


def test_empty_swagger():
    """Test minimal Swagger spec"""
    swagger = {"openapi": "3.0.0"}
    result = parse_swagger_spec(json.dumps(swagger))
    assert result['title'] == 'Unknown'
    assert result['endpoint_count'] == 0
    print("✓ Empty Swagger test PASSED")


if __name__ == '__main__':
    print("\n🧪 Running Swagger parser tests...\n")
    try:
        test_valid_swagger()
        test_swagger_without_servers()
        test_invalid_json()
        test_empty_swagger()
        print("\n✅ All Swagger parser tests passed!\n")
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}\n")
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
