# Number Classification API

## Overview
The **Number Classification API** is a RESTful API that accepts a number as input and returns interesting mathematical properties about it, along with a fun fact. The API supports:

- Checking if a number is **prime**
- Checking if a number is **perfect**
- Checking if a number is **Armstrong**
- Determining if the number is **odd or even**
- Calculating the **sum of its digits**
- Providing a **fun fact** about the number from an external API

## Features
- **Technology Stack:** Python, Flask, Flask-CORS, Requests
- **Publicly Accessible API**
- **JSON Response Format**
- **Error Handling & Validation**
- **CORS Handling for Cross-Origin Requests**

## API Endpoint

### Base URL:
```
<your-deployed-url>/api/classify-number?number=<number>
```

### Request Method:
**GET**

### Example Request:
```
GET <your-deployed-url>/api/classify-number?number=371
```

### Response Format:
#### **Success Response (200 OK)**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### **Error Response (400 Bad Request)**
```json
{
    "number": "invalid_input",
    "error": true
}
```

## Installation & Setup

### Prerequisites
Ensure you have **Python 3.7+** installed.

### Install Dependencies
```bash
pip install flask flask-cors requests
```

### Run Locally
```bash
python app.py
```
API will be available at: `http://127.0.0.1:5000/api/classify-number?number=<your_number>`

## Deployment
### Deploy on Render
1. Push your code to **GitHub**
2. Create an account on **Render.com**
3. Deploy as a **Web Service**
4. Set `Start Command`: `gunicorn app:app`
5. Add `PORT=5000` in environment variables

### Deploy on Railway (Alternative)
1. Sign up on **Railway.app**
2. Link your **GitHub repository**
3. Add environment variable `PORT=5000`
4. Deploy 🚀

## Usage Example
### Using cURL
```bash
curl -X GET "http://127.0.0.1:5000/api/classify-number?number=371"
```

### Using Postman
1. Open Postman
2. Select `GET` method
3. Enter URL: `http://127.0.0.1:5000/api/classify-number?number=371`
4. Click **Send**

## Deployed end point
https://numbers-api-6n3m.onrender.com

## Link to github Repository
https://github.com/Pascal509/Numbers_API

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License
This project is licensed under the **MIT License**.

## Contact
For any inquiries, reach out at: [Your Email] or visit the **GitHub Repository**: [Your Repo Link]

