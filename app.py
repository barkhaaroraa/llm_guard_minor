from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import redis
import re

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure Redis for Rate Limiting
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Initialize Flask-Limiter with Redis storage
limiter = Limiter(
    key_func=get_remote_address,
    storage_uri="redis://localhost:6379"
)
limiter.init_app(app)

# Function to sanitize input text
def sanitize_text(text):
    text = re.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", "[EMAIL]", text)
    text = re.sub(r"\b\d{10}\b", "[PHONE]", text)  
    text = re.sub(r"\b\d{3} \d{3} \d{4}\b", "[PHONE]", text)  
    return text

# Rate-limited API route (max 5 requests per minute per user)
@app.route('/api/process-text', methods=['POST'])
@limiter.limit("10 per minute")  # 5 requests per minute
def process_text():
    data = request.json
    text = data.get('text', '')

    processed_text = sanitize_text(text)
    
    return jsonify({
        'processed_text': processed_text,
        'status': 'success'
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
