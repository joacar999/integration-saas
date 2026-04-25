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
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": """You are a senior Python integration engineer.

Given this OpenAPI/Swagger specification, generate a production-ready Python integration module.

Requirements:
- Use requests library
- Create clean functions per endpoint
- Include authentication placeholder (API key or token)
- Add proper error handling (status codes)
- Add logging
- Use type hints
- No unnecessary explanations

Output ONLY valid Python code."""
                },
                {
                    "role": "user",
                    "content": f"Here is the OpenAPI spec:\n{swagger_spec}"
                }
            ],
            temperature=0.3,
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
