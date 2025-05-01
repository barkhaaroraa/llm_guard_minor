from flask import Flask, request, jsonify
from flask_cors import CORS
from rate_limiting import create_limiter

# Import your custom packages
from sanitize import sanitize_text
from invisible import (
    remove_invisible_characters,
    has_invisible_characters,
    find_invisible_characters,
    decode_from_tag_chars
)
from ban_topics import is_prompt_unsafe

# Flask App
app = Flask(__name__)
CORS(app)

# Rate Limiting
limiter = create_limiter(app)

# API Route
@app.route('/api/process-text', methods=['POST'])
@limiter.limit("5 per minute")  # Rate limit, 5 requests per minute

def process_text():
    data = request.json
    text = data.get('text', '')  # Retrieve text from the JSON payload

    # Step 1: Anonymization (Sanitization)
    sanitized = sanitize_text(text)
    
    # Step 2: Invisible Text Handling
    has_invis = has_invisible_characters(sanitized)
    details = find_invisible_characters(sanitized)
    decoded = decode_from_tag_chars(sanitized)
    cleaned = remove_invisible_characters(sanitized)

    # Step 3: Banning Unsafe Topics
    banned = is_prompt_unsafe(cleaned)

    # Modify return statement based on whether a banned topic is detected
    if banned:
        return jsonify({
            "status": "success",
            "final_output": "banned topic detected",  # Return message if banned topic is detected
            "has_invisible_characters": has_invis,
            "invisible_details": details,
            "unsafe_prompt_detected": banned
        })
    else:
        return jsonify({
            "status": "success",
            "final_output": cleaned,  # Return cleaned text if no banned topic detected
            "has_invisible_characters": has_invis,
            "invisible_details": details,
            "unsafe_prompt_detected": banned
        })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
