from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)  

def sanitize_text(text):
    text = re.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", "[EMAIL]", text)
    
    
    text = re.sub(r"\b\d{10}\b", "[PHONE]", text)  
    text = re.sub(r"\b\d{3} \d{3} \d{4}\b", "[PHONE]", text)  
    
    return text

@app.route('/api/process-text', methods=['POST'])
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