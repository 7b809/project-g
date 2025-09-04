from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

# Load API key
api_key = os.getenv("GEMINI_API")
genai.configure(api_key=api_key)

# Flask app
app = Flask(__name__)
CORS(app)

# ---------------------------
# One list of models (priority order)
# ---------------------------
ALL_MODELS = [
    "gemini-2.5-pro",
    "gemini-2.5-flash",
    "gemini-1.5-pro",
    "gemini-1.5-flash",
    "gemini-pro"
]

# ---------------------------
# Model fallback helper
# ---------------------------
def generate_with_fallback(prompt):
    """
    Try generating with each model in ALL_MODELS until one succeeds.
    Returns (response.text, model_name) or error message.
    """
    for model_name in ALL_MODELS:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            if response and response.text:
                return response.text, model_name
        except Exception as e:
            print(f"⚠️ Model {model_name} failed: {str(e)}")
            continue
    return "❌ All models failed. Please try again later.", None

# ---------------------------
# Home route
# ---------------------------
@app.route("/")
def home():
    return jsonify({"message": "🚀 Server running successfully!"})

# ---------------------------
# Route for Todo tasks
# ---------------------------
@app.route("/todo", methods=["GET"])
def todo_route():
    code = request.args.get("code")
    if not code:
        return jsonify({"error": "❌ Please provide 'code' query param"}), 400

    prompt = f"""
    You are a helpful coding assistant. 
    The following React code contains TODO comments. 
    Please complete the TODOs and return only the fixed code:

    {code}
    """

    response_text, used_model = generate_with_fallback(prompt)
    return jsonify({
        "todo_suggestion": response_text,
        "model_used": used_model
    })

# ---------------------------
# Route for Debugging tasks
# ---------------------------
@app.route("/debug", methods=["GET"])
def debug_route():
    code = request.args.get("code")
    if not code:
        return jsonify({"error": "❌ Please provide 'code' query param"}), 400

    prompt = f"Debug and fix issues in this code:\n\n{code}"

    response_text, used_model = generate_with_fallback(prompt)
    return jsonify({
        "debug_suggestion": response_text,
        "model_used": used_model
    })

# ---------------------------
# Route for custom prompts
# ---------------------------
@app.route("/prompt", methods=["GET"])
def prompt_route():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "❌ Please provide 'q' query param"}), 400

    response_text, used_model = generate_with_fallback(query)
    return jsonify({
        "response": response_text,
        "model_used": used_model
    })

# ---------------------------
# Run server
# ---------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
