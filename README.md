
# Gemini AI Flask Server

This is a Flask-based AI server using **Google Gemini API** (`google.generativeai`) to provide coding assistance, debugging help, and custom prompt responses. The server is deployed at:

**URL:** [https://project-g-psi.vercel.app/](https://project-g-psi.vercel.app/)

---

## 🛠️ Features

- **Coding TODO assistant:** Automatically complete TODOs in your code.
- **Debugging assistant:** Detect and fix issues in your code.
- **Custom prompts:** Ask any question or prompt to the AI.
- **Model fallback:** Uses multiple Gemini models in priority order for reliability.

---

## ⚙️ API Endpoints

All endpoints are **GET** requests and return JSON responses.

### 1. Home

**URL:** `/`  
**Description:** Check if the server is running.

**Request Example:**

```bash
curl https://project-g-psi.vercel.app/
```

**Response Example:**

```json
{
  "message": "🚀 Server running successfully!"
}
```

---

### 2. TODO Assistant

**URL:** `/todo`  
**Description:** Auto-complete TODO comments in your code.  

**Query Parameters:**

| Parameter | Type   | Required | Description                       |
|-----------|--------|----------|-----------------------------------|
| `code`    | string | Yes      | The code snippet containing TODOs |

**Request Example:**

```bash
curl "https://project-g-psi.vercel.app/todo?code=print('Hello World')"
```

**Response Example:**

```json
{
  "todo_suggestion": "print('Hello World')  # TODO completed",
  "model_used": "gemini-2.5-pro"
}
```

---

### 3. Debugging Assistant

**URL:** `/debug`  
**Description:** Debug and fix issues in your code.

**Query Parameters:**

| Parameter | Type   | Required | Description             |
|-----------|--------|----------|-------------------------|
| `code`    | string | Yes      | The code snippet to debug |

**Request Example:**

```bash
curl "https://project-g-psi.vercel.app/debug?code=prin('Hello')"
```

**Response Example:**

```json
{
  "debug_suggestion": "print('Hello')",
  "model_used": "gemini-2.5-flash"
}
```

---

### 4. Custom Prompt

**URL:** `/prompt`  
**Description:** Send any custom prompt to the AI and get a response.

**Query Parameters:**

| Parameter | Type   | Required | Description           |
|-----------|--------|----------|-----------------------|
| `q`       | string | Yes      | Your custom prompt    |

**Request Example:**

```bash
curl "https://project-g-psi.vercel.app/prompt?q=Explain%20quantum%20entanglement"
```

**Response Example:**

```json
{
  "response": "Quantum entanglement is a physical phenomenon...",
  "model_used": "gemini-1.5-pro"
}
```

---

## ⚠️ Error Handling

- If the required query parameter is missing:

```json
{
  "error": "❌ Please provide 'code' query param"
}
```

or

```json
{
  "error": "❌ Please provide 'q' query param"
}
```

- If all models fail:

```json
{
  "todo_suggestion": "❌ All models failed. Please try again later.",
  "model_used": null
}
```

---

## 🧪 Usage Notes

- **Recommended Tools:** Postman, Thunder Client, cURL
- **Headers:** No special headers required, but `Accept: application/json` can be added.
- **Query Encoding:** URL-encode your `code` or `q` parameter to avoid errors.

---

### Example Workflow (Postman / Thunder Client)

1. **TODO Completion**
   - Method: GET
   - URL: `https://project-g-psi.vercel.app/todo?code=print("TODO")`
   - Response: JSON with completed TODO code.

2. **Debugging**
   - Method: GET
   - URL: `https://project-g-psi.vercel.app/debug?code=prin("Hello")`
   - Response: JSON with fixed code.

3. **Custom Prompt**
   - Method: GET
   - URL: `https://project-g-psi.vercel.app/prompt?q=What%20is%20Python%20decorator?`
   - Response: JSON with AI-generated answer.

---

## ✅ Model Fallback Order

The server tries the following Gemini models in priority order:

1. `gemini-2.5-pro`
2. `gemini-2.5-flash`
3. `gemini-1.5-pro`
4. `gemini-1.5-flash`
5. `gemini-pro`

The first model that successfully generates content will be returned.

---

## 🔑 Environment Variables

- `GEMINI_API`: Your Google Gemini API key must be set in the environment.

Example:

```bash
export GEMINI_API="YOUR_API_KEY_HERE"
```

---

## 📦 Deployment

- The app is deployed on Vercel.
- URL: [https://project-g-psi.vercel.app/](https://project-g-psi.vercel.app/)
- Flask app runs on port 5000 internally but Vercel handles routing automatically.

---

## 💡 Notes

- Ensure your code or prompt is URL-encoded when using GET requests.
- The server returns JSON only.
- You can integrate these endpoints into any frontend or IDE plugin for live coding assistance.

---
