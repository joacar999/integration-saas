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

# ===================== AI SYSTEM PROMPT START =====================
SYSTEM_PROMPT = """You are a senior Python integration engineer.

Generate ONLY raw Python source code.
Do not use Markdown.
Do not wrap the output in triple backticks.
Do not include explanations outside Python comments.

Given this OpenAPI/Swagger specification, generate a production-ready Python client library.

Requirements:
- Use requests
- Create a class-based API client
- One method per endpoint
- Include API key/token authentication placeholder
- Add robust error handling
- Raise exceptions for HTTP errors
- Add logging
- Use type hints
- Use readable method names
- Include a small if __name__ == "__main__" usage example
- Output must be directly saveable and runnable as a .py file
- Use correct endpoint paths and parameters from the OpenAPI spec
- Ensure URLs and query parameters match the specification exactly
- Include request timeout (e.g. timeout=10)

Return ONLY valid Python code."""
# ===================== AI SYSTEM PROMPT END =====================


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

        # Call OpenAI with system prompt and Swagger spec
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
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
