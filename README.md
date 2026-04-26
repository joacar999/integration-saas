# 🚀 Concilio Design – Integration Studio

### Generate **runnable Python API clients** from OpenAPI specs — instantly

---

## ⚡ Stop writing API integrations manually

Paste an OpenAPI spec → get a **working Python client with example usage and dependencies**.

No boilerplate. No docs digging. No guessing.

---

## 🎬 How it works

```text
1. Paste OpenAPI JSON or URL
2. Click "Generate"
3. Download Python client
4. Run it immediately
```

```bash
python generated_client.py
```

---

## ✨ What you get

Every generated client includes:

* ✅ Correct **base URL from OpenAPI spec**
* ✅ One method per endpoint
* ✅ **Error handling + logging**
* ✅ **Request timeouts**
* ✅ **Runnable example (safe GET when possible)**
* ✅ Embedded **requirements.txt**
* ✅ Clean, readable Python code

---

## 🧪 Example (real output)

```python
client = PetstoreClient(api_key="your_api_key")

result = client.get_pet_by_id(1)
print(result)
```

👉 This is not pseudo-code. It runs.

---

## 🎯 Why use this?

Instead of:

* ❌ Reading API docs
* ❌ Writing repetitive request code
* ❌ Debugging HTTP issues

You get:

* ✅ Instant working integration
* ✅ Consistent client structure
* ✅ Faster prototyping

---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/ai-integration-saas.git
cd ai-integration-saas

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt
```

---

## 🔐 OpenAI API Key

Get your key:

👉 https://platform.openai.com/api-keys

Create `.env`:

```env
OPENAI_API_KEY=sk-xxxxxxxx
```

---

## ▶️ Run locally

```bash
python app.py
```

Open:

```
http://localhost:5000
```

---

## 🧪 Usage

Paste either:

### JSON

```json
{ "openapi": "3.0.0", ... }
```

### OR URL (recommended)

```
https://petstore3.swagger.io/api/v3/openapi.json
```

---

## ⚠️ Limitations (MVP)

* JSON only (YAML not supported yet)
* Large specs are truncated
* Some APIs require manual auth setup

---

## 🔌 API

### `POST /generate`

**Request**

```json
{
  "swagger_spec": "https://example.com/openapi.json"
}
```

**Response**

```json
{
  "success": true,
  "generated_code": "...",
  "api_name": "Example API",
  "endpoints_found": 1
}
```

---

## 🚀 Deployment (Railway)

1. Push repo
2. Connect in Railway
3. Add environment variable:

```
OPENAI_API_KEY=sk-xxxx
```

4. Deploy

---

## 🧠 Roadmap

* [ ] YAML support
* [ ] Full spec support (no truncation)
* [ ] Multi-file output (client + requirements.txt)
* [ ] Test generation
* [ ] Documentation generation
* [ ] UI improvements
* [ ] SaaS accounts
* [ ] Payments

---

## 💰 Early validation

Current approach:

> “We generate a Python SDK from your API for 500 SEK”

---

## 💡 One-liner

> Stop writing API clients. Generate them.

---

## 📬 Contact

Concilio Design AB

www.conciliodesign.se
info@conciliodesign.se


---

**Status**: MVP Live
**Version**: 0.3
