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
    return n == sum(i for i in range(1, n) if n % i == 0)

def is_armstrong(n):
    """Check if a number is a armstrong number."""
    digits = [int(digit) for digit in str(n)]
    return sum(d ** len(digits) for d in digits) == n

@app.route("/api/classify-number", methods=["GET"])
def classify_number():
    """API endpoint to classify a number and return its properties."""
    number = request.args.get("number")

    if number is None or not number.isdigit():
        return jsonify({"number": number, "error": True}), 400
    
    num = int(number)
    properties = []

    if is_prime(num):
        properties.append("prime")
    if is_perfect(num):
        properties.append("perfect")
    if is_armstrong(num):
        properties.append("armstrong")

    properties.append("even" if num % 2 == 0 else "odd")

    digit_sum = sum(int(d) for d in str(num))

    # Fetch fun fact from Numbers API
    fun_fact = f"{num} is a unique number."
    try:
        response = requests.get(f"http://numbersapi.com/{num}")
        if response.status_code == 200:
            fun_fact = response.text
    except requests.exceptions.RequestException:
        pass  # Use default fun fact if API fails

    return jsonify({
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
