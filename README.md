# AI Integration Workflows - SaaS MVP

Transform Swagger/OpenAPI specs into Python integration examples using AI.

## Features

✨ **AI-Powered Code Generation**
- Upload Swagger/OpenAPI JSON specifications
- Automatically generate production-ready Python integration code
- Includes setup, examples, and error handling

🎯 **Key Benefits**
- Save hours on API integration documentation
- Consistent, high-quality Python examples
- Support for any REST API with an OpenAPI spec

## Tech Stack

- **Backend**: Flask (Python)
- **AI**: OpenAI GPT-4
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Database**: (Coming soon)

## Installation

### Prerequisites
- Python 3.8+
- OpenAI API key (get one at https://platform.openai.com/api-keys)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-integration-saas.git
cd ai-integration-saas
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment:
```bash
# Create .env file
echo OPENAI_API_KEY=your_api_key_here > .env
```

5. Run the application:
```bash
python app.py
```

6. Open browser: http://localhost:5000

## Usage

1. **Paste Swagger/OpenAPI JSON** in the textarea
2. Click **"✨ Generate Python Examples"**
3. Wait for AI to generate integration code
4. **Download** the `.py` file
5. Use the generated code in your project

## Project Structure

```
ai-integration-saas/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not in git)
├── .gitignore            # Git ignore file
├── README.md             # This file
├── templates/
│   └── index.html        # Web UI
└── tests/
    ├── test_app.py       # Flask endpoint tests
    ├── test_swagger_parser.py  # Swagger parsing tests
    ├── test_manual.py    # Manual integration test
    └── sample_swagger.json     # Example Swagger spec
```

## Testing

Run all tests:
```bash
python tests/test_app.py
python tests/test_swagger_parser.py
```

## API Endpoints

### `GET /`
Returns the web interface

### `POST /generate`
Generates Python integration code

**Request:**
```json
{
  "swagger_spec": "{... Swagger JSON ...}"
}
```

**Response:**
```json
{
  "success": true,
  "generated_code": "import requests\n...",
  "api_name": "Weather API",
  "endpoints_found": 2
}
```

## Pricing (Future)

- **Free**: 3 generations/month
- **Pro**: $19/month - 200 generations/month
- **Enterprise**: $49/month - Unlimited + priority support

## Roadmap

- [ ] Database for saving specs and generations
- [ ] User authentication + accounts
- [ ] Stripe payment integration
- [ ] API rate limiting
- [ ] Advanced documentation generation
- [ ] Support for GraphQL
- [ ] Deploy to production (Heroku/Railway)

## Contributing

Feel free to fork, improve, and submit PRs!

## License

MIT License - see LICENSE file

## Support

For issues, questions, or feature requests: create an issue on GitHub

---

**Status**: MVP Complete ✅  
**Last Updated**: April 2026  
**Version**: 0.1.0
