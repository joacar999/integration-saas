# Concilio Design – Integration Studio

Turn OpenAPI specs into production-ready Python clients in seconds.

---

## 🚀 What is this?

**Integration Studio** is a lightweight SaaS tool that generates Python API clients directly from Swagger/OpenAPI specifications.

Paste a JSON spec → get a ready-to-use `.py` integration module.

---

## ✨ Features

* Generate **production-ready Python clients**
* One method per endpoint
* Built-in **error handling and logging**
* Supports any REST API with OpenAPI/Swagger
* Download ready-to-run `.py` files

---

## 🎯 Why use this?

* Save hours on manual API integration
* Avoid boilerplate and repetitive coding
* Get consistent, structured client code
* Quickly prototype integrations

---

## 🛠 Tech Stack

* **Backend**: Flask (Python)
* **AI**: OpenAI GPT-4o
* **Frontend**: HTML, CSS, Vanilla JS
* **Deployment**: Railway

---

## ⚙️ Installation

### 1. Clone repo

```bash
git clone https://github.com/yourusername/ai-integration-saas.git
cd ai-integration-saas
```

---

### 2. Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 OpenAI API Key Setup

You need an API key from OpenAI:

👉 https://platform.openai.com/api-keys

### Steps

1. Log in
2. Click **"Create new secret key"**
3. Copy the key (shown only once)

---

### 4. Configure environment

Create `.env` file:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
```

---

### 5. Run the app

```bash
python app.py
```

Open in browser:

```
http://localhost:5000
```

---

## 🧪 Usage

1. Paste an **OpenAPI/Swagger JSON**
2. Click **Generate**
3. Download generated Python file
4. Run or integrate into your project

---

## ⚠️ Important Notes

* Only **JSON** OpenAPI specs are supported (not YAML)
* Large specs are automatically truncated to avoid token limits
* Generated clients may require minor adjustments depending on API

---

## 🧱 Project Structure

```
ai-integration-saas/
├── app.py
├── requirements.txt
├── .env
├── templates/
│   └── index.html
├── static/
│   └── logo.png
├── tests/
└── README.md
```

---

## 🔌 API Endpoints

### `GET /`

Returns UI

### `POST /generate`

**Request**

```json
{
  "swagger_spec": "{...json...}"
}
```

**Response**

```json
{
  "success": true,
  "generated_code": "...",
  "api_name": "Example API",
  "endpoints_found": 5
}
```

---

## 🚀 Deployment (Railway)

1. Push to GitHub
2. Connect repo in Railway
3. Add environment variable:

```
OPENAI_API_KEY=sk-xxxx
```

4. Deploy

---

## 🧠 Roadmap

* [ ] Support YAML specs
* [ ] Full spec handling (no truncation)
* [ ] Test suite generation
* [ ] Multiple output formats (SDK, docs, tests)
* [ ] User accounts & history
* [ ] Payment integration

---

## 💰 Monetization (Early Stage)

Current validation approach:

* Manual generation: ~500 SEK per API client
* Later:

  * Free tier (limited generations)
  * Pro plan (monthly usage)
  * Enterprise options

---

## 🤝 Contributing

PRs welcome — especially improvements to:

* Prompt engineering
* UI/UX
* API parsing
* Output quality

---

## 📄 License

MIT

---

## 📬 Contact

Concilio Design

---

**Status**: MVP Live
**Version**: 0.2
