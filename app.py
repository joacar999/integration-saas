from flask import Flask, render_template, request, jsonify
import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Check if API key is set
api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    client = OpenAI(api_key=api_key)
else:
    client = None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    try:
        # Check if OpenAI API key is set
        if not client:
            return jsonify({
                'error': 'OpenAI API key not configured. Please set OPENAI_API_KEY in .env file'
            }), 503
        
        data = request.json
        swagger_spec = data.get('swagger_spec')

        if not swagger_spec:
            return jsonify({'error': 'No Swagger spec provided'}), 400

        # Parse Swagger JSON
        try:
            spec = json.loads(swagger_spec)
        except json.JSONDecodeError:
            return jsonify({'error': 'Invalid JSON'}), 400

        # Extract key info
        title = spec.get('info', {}).get('title', 'API')
        base_url = spec.get('servers', [{}])[0].get(
            'url', 'https://api.example.com')
        paths = spec.get('paths', {})

        # Build prompt for OpenAI
        endpoint_summary = f"API Title: {title}\nBase URL: {base_url}\n\nEndpoints:\n"
        for path, methods in list(paths.items())[:5]:  # First 5 endpoints
            endpoint_summary += f"- {path}: {', '.join(methods.keys())}\n"

        prompt = f"""Generate Python integration examples for these API endpoints:

{endpoint_summary}

Provide:
1. Setup/authentication code
2. Example requests for each endpoint
3. Error handling

Code should use the `requests` library."""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a Python API integration expert. Generate practical, working code examples."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )

        generated_code = response.choices[0].message.content

        return jsonify({
            'success': True,
            'generated_code': generated_code,
            'api_name': title,
            'endpoints_found': len(paths)
        })

    except Exception as e:
        print(f"Error in /generate: {str(e)}")  # Log for debugging
        return jsonify({'error': f'Generation error: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
