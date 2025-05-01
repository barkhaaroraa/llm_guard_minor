from flask import Flask, request, jsonify
from flask_cors import CORS

# Import your custom packages
from rate_limiting import limiting
from sanitize import sanitize_text

from invisible import (
    remove_invisible_characters,
    has_invisible_characters,
    find_invisible_characters
)

# Flask App
app = Flask(__name__)
CORS(app)

# Rate Limiting
limiter = limiting(app)

# API Route
@app.route('/api/process-text', methods=['POST'])
@limiter.limit("5 per minute")
def process_text():
    data = request.json
    text = data.get('text', '')

    sanitized = sanitize_text(text)
    has_invis = has_invisible_characters(sanitized)
    details = find_invisible_characters(sanitized)
    cleaned = remove_invisible_characters(sanitized)

    return jsonify({
        "status": "success",
        "original_text": text,
        "sanitized_text": sanitized,
        "has_invisible_characters": has_invis,
        "cleaned_text": cleaned,
        "invisible_details": details
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
