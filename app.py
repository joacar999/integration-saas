from flask import Flask, render_template, request, jsonify
import json
import os
from openai import OpenAI
from dotenv import load_dotenv
import requests

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
- Strictly follow the OpenAPI specification
- Do not invent endpoints or parameters
- Use the exact paths and parameter names defined in the spec
- If unsure, prefer correctness over assumptions
- Always include the correct full base URL from the OpenAPI servers section
- Do not use relative base URLs unless the spec only provides relative URLs
- Include a clearly marked requirements.txt section as Python comments
- Include a runnable example using a safe GET endpoint when available
- Prefer GET endpoints for the example because they are safer to test
- If authentication is required, use a placeholder API key
- Include a comment showing exactly how to install dependencies, e.g.: pip install requests python-dotenv

Output format:
1. First output the Python client code
2. At the bottom, include this comment block:

# ===================== requirements.txt =====================
# requests
# python-dotenv
# ============================================================

Return ONLY valid Python code."""
# ===================== AI SYSTEM PROMPT END =====================


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    try:
        # Check if OpenAI API key is set
        if not client:
            return (
                jsonify(
                    {
                        "error": "OpenAI API key not configured. Please set OPENAI_API_KEY in .env file"
                    }
                ),
                503,
            )

        data = request.json
        swagger_spec = data.get("swagger_spec")

        if not swagger_spec:
            return jsonify({"error": "No Swagger spec provided"}), 400

        # Parse Swagger JSON
        try:
            # If input is a URL, fetch it
            if swagger_spec.startswith("http"):
                response = requests.get(swagger_spec)
                response.raise_for_status()
                spec = response.json()
            else:
                spec = json.loads(swagger_spec)

        except json.JSONDecodeError:
            return jsonify({"error": "Invalid JSON"}), 400

        # Extract key info
        title = spec.get("info", {}).get("title", "API")
        paths = spec.get("paths", {})

        # Limit size to avoid token overflow
        //paths = dict(list(paths.items())[:1])
        
        # Prefer one safe GET endpoint to make generated examples runnable
        selected_paths = {}

        for path, methods in paths.items():
            get_method = methods.get("get")
            if get_method:
                selected_paths[path] = {"get": get_method}
                break

        # Fallback: if no GET endpoint exists, use first endpoint
        if not selected_paths:
            selected_paths = dict(list(paths.items())[:1])

        paths = selected_paths
        ///////////////////////////////////////
        limited_spec = {
            "openapi": spec.get("openapi"),
            "info": spec.get("info", {}),
            "servers": spec.get("servers", []),
            "paths": paths,
        }

        limited_swagger_spec = json.dumps(limited_spec, indent=2)
        # Call OpenAI with system prompt and Swagger spec
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": f"""Here is the OpenAPI spec:
                    {limited_swagger_spec}
                    IMPORTANT:
                    Carefully read the specification.
                    Extract exact endpoint paths and parameters.
                    Do not guess or simplify anything.
                    Use the specification exactly as provided.
                    Prefer the HTTPS server URL from the "servers" section.
                    Do not use legacy or alternative hostnames.
                    Do not add Authorization headers unless security requirements are explicitly defined in the spec.
                    Use a GET endpoint in the runnable example if one exists.
                    """,
                },
            ],
            temperature=0.3,
            max_tokens=2000,
        )

        generated_code = response.choices[0].message.content

        return jsonify(
            {
                "success": True,
                "generated_code": generated_code,
                "api_name": title,
                "endpoints_found": len(paths),
            }
        )

    except Exception as e:
        print(f"Error in /generate: {str(e)}")  # Log for debugging
        return jsonify({"error": f"Generation error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
