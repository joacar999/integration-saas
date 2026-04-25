"""Manual integration test - use this to test the full flow"""
import json
import sys
import os

# Läs example Swagger spec


def load_sample_swagger():
    """Load sample Swagger JSON"""
    current_dir = os.path.dirname(__file__)
    with open(os.path.join(current_dir, 'sample_swagger.json'), 'r') as f:
        return f.read()


def test_full_flow():
    """Test the complete flow: Swagger → Parse → Generate"""
    print("\n📋 Loading sample Swagger spec...")
    swagger_content = load_sample_swagger()
    spec = json.loads(swagger_content)

    print(f"✓ Loaded: {spec['info']['title']}")
    print(f"  Base URL: {spec['servers'][0]['url']}")
    print(f"  Endpoints: {len(spec['paths'])}")

    for path in spec['paths'].keys():
        print(f"    - {path}")

    print("\n💡 Next steps:")
    print("  1. Copy the Swagger JSON above")
    print("  2. Run: python app.py")
    print("  3. Go to: http://localhost:5000")
    print("  4. Paste the JSON and click 'Generate Python Examples'")
    print("  5. Download the generated Python integration code")


if __name__ == '__main__':
    print("\n🧪 Manual Integration Test\n")
    try:
        test_full_flow()
        print("\n✅ Test completed!\n")
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
