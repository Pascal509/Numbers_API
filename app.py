from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

def is_prime(n):
    """Check if number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def is_perfect(n):
    """Check if a number is a perfect number."""
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    """Check if a number is a armstrong number."""
    digits = [int(digit) for digit in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

# Function to fetch a fun fact from Numbers API
def get_fun_fact(n):
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math")
        if response.status_code == 200:
            return response.text
        return "No fun fact available."
    except:
        return "No fun fact available."

@app.route("/api/classify-number", methods=["GET"])
def classify_number():
    """API endpoint to classify a number and return its properties."""
    number = request.args.get("number")

    if number is None or not number.isdigit():
        return jsonify({"number": number, "error": True}), 400
    
    num = int(number)

    #Determine properties
    properties = []

    if is_armstrong(num):
        properties.append("armstrong")
    properties.append("odd" if num % 2 != 0 else "even")

    response = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(num)),
        "fun_fact": get_fun_fact(num)
    }

    return jsonify(response), 200
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
