import requests

def test_rate_limiting():
    url = "http://127.0.0.1:5000/api/process-text"
    data = {"text": "Test email: example@email.com"}

    for i in range(7):  # Try sending 7 requests
        response = requests.post(url, json=data)
        
        # Check if response is JSON, otherwise print raw response
        try:
            json_response = response.json()
        except requests.exceptions.JSONDecodeError:
            json_response = {"error": "Non-JSON response", "status_code": response.status_code, "text": response.text}
        
        print(f"Attempt {i+1}: {json_response}")

test_rate_limiting()
