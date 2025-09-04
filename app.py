from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import json, os

# Load API key
api_key = os.getenv("GEMINI_API")
genai.configure(api_key=api_key)

# Flask app
app = Flask(__name__)
CORS(app)

# Home route
@app.route("/")
def home():
    return jsonify({"message": "🚀 Server running successfully!"})

# Route for Todo tasks
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
    model = genai.GenerativeModel("gemini-2.5-flash")  # 🔄 upgraded model
    response = model.generate_content(prompt)
    return jsonify({"todo_suggestion": response.text})

# Route for Debugging tasks
@app.route("/debug", methods=["GET"])
def debug_route():
    code = request.args.get("code")
    if not code:
        return jsonify({"error": "❌ Please provide 'code' query param"}), 400

    model = genai.GenerativeModel("gemini-2.5-pro")  # 🔄 using Pro for better debugging
    response = model.generate_content(f"Debug and fix issues in this code:\n\n{code}")
    return jsonify({"debug_suggestion": response.text})

# Route for custom prompts
@app.route("/prompt", methods=["GET"])
def prompt_route():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "❌ Please provide 'q' query param"}), 400

    model = genai.GenerativeModel("gemini-2.5-flash")  # 🔄 lightweight for general prompts
    response = model.generate_content(query)
    return jsonify({"response": response.text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
