FastAPI Quiz Generator API 🎯
https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
https://img.shields.io/badge/License-MIT-blue.svg

A high-performance REST API for generating customizable quizzes and MCQ tests, built with FastAPI. This API serves as a backend for educational platforms, mobile apps, and web applications requiring dynamic quiz generation.

✨ Features
🎯 Dynamic Quiz Generation: Create custom quizzes based on test type, categories, and question count

🔐 Secure Authentication: HTTP Basic Auth with role-based access (users & admin)

📝 Admin Question Management: Add new questions to the database via API

🎲 Intelligent Randomization: Unique quiz experiences with shuffled questions

📊 CSV Data Integration: Efficient question storage and retrieval

📚 Interactive Documentation: Auto-generated OpenAPI/Swagger UI

⚡ High Performance: Async support for concurrent requests

🔍 Input Validation: Comprehensive parameter validation with clear errors

🔄 CORS Support: Ready for web application integration

🚀 Quick Start
Prerequisites
Python 3.8+

pip

Installation
Clone the repository

bash
git clone https://github.com/yourusername/fastapi-quiz-api.git
cd fastapi-quiz-api
Create and activate virtual environment

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
pip install -r requirements.txt
Start the server

bash
uvicorn main:app --reload
The API will be available at http://localhost:8000

📖 API Documentation
Once the server is running, access the interactive documentation:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

🔑 Authentication
The API uses HTTP Basic Authentication. Available credentials:

Username	Password	Role
alice	wonderland	User
bob	builder	User
clementine	mandarine	User
admin	4dm1N	Administrator
Example Authorization Header:

text
Authorization: Basic YWxpY2U6d29uZGVybGFuZA==
📡 API Endpoints
GET /verify
Health check endpoint to verify API functionality.

Response:

json
{
  "message": "API is functional."
}
POST /generate_quiz
Generate a custom quiz with specified parameters.

Request:

json
{
  "test_type": "multiple_choice",
  "categories": ["math", "history"],
  "number_of_questions": 10
}
Response: Array of question objects with question text, options, and correct answers.

POST /create_question
Add a new question to the database (Admin only).

Request:

json
{
  "admin_username": "admin",
  "admin_password": "4dm1N",
  "question": "What is the capital of Germany?",
  "subject": "geography",
  "correct": ["Berlin"],
  "use": "multiple_choice",
  "responseA": "Munich",
  "responseB": "Berlin",
  "responseC": "Hamburg",
  "responseD": "Cologne"
}
📁 Project Structure
text
fastapi-quiz-api/
├── main.py                 # FastAPI application
├── questions.csv           # Question database (CSV format)
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── tests/                 # Test suite (optional)
    └── test_api.py
🧪 Running Tests
bash
# Install test dependencies
pip install pytest httpx

# Run tests
pytest tests/
🐳 Docker Support
bash
# Build the Docker image
docker build -t fastapi-quiz-api .

# Run the container
docker run -p 8000:8000 fastapi-quiz-api
📊 Data Model
The questions are stored in questions.csv with the following columns:

Column	Description
question	Question text
subject	Category (math, history, geography, etc.)
correct	Comma-separated correct answers
use	Test type (multiple_choice, etc.)
responseA-D	Multiple choice options
🔧 Configuration
Default configuration can be modified in main.py:

Authentication credentials

Question limits

CORS origins

Server settings

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Built with FastAPI

Interactive docs powered by Swagger UI

Inspired by educational technology needs

📞 Support
For support, please open an issue in the GitHub repository or contact the maintainers.

Made with ❤️ for the developer community

If you find this project helpful, please consider giving it a ⭐ on GitHub!
