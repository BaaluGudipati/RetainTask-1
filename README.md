# User Management API — Refactored Version

## Overview
This is a refactored version of a legacy User Management API. The task focused on fixing critical code issues, improving security, organizing the codebase, and maintaining the API’s core functionality.

## How to Run

### Prerequisites
- Python 3.8+
- SQLite3 (comes with Python)
- pip (Python package manager)

### Setup Instructions
```bash
pip install -r requirements.txt
python init_db.py
python app.py
The API will be available at: http://localhost:5009

API Endpoints
Endpoint	Method	Description
/	GET	Health Check
/users	GET	Get all users
/user/<id>	GET	Get user by ID
/users	POST	Create new user
/user/<id>	PUT	Update user details
/user/<id>	DELETE	Delete user
/search?name=<name>	GET	Search users by name
/login	POST	User login

Project Structure
Copy
Edit
messy-migration/
├── app.py
├── init_db.py
├── requirements.txt
├── CHANGES.md
├── README.md
├── models/
│   └── user_model.py
├── routes/
│   └── user_routes.py
└── utils/
    ├── auth.py
    └── validators.py
Changes & Improvements
All refactoring decisions and improvements are documented in CHANGES.md. Below is a summary of major fixes implemented in the codebase:

Passwords are now securely hashed using PBKDF2-SHA256 instead of being stored as plaintext.

SQL Injection vulnerabilities fixed by replacing unsafe raw queries with parameterized queries.

Codebase modularized — Separated routes, models, and utility functions into respective folders for better structure.

Database connections handled per request to ensure thread-safety and avoid global DB connection issues.

Added input validation for creating, updating, and logging in users to prevent invalid or malicious data entries.

API responses have been standardized using JSON responses and correct HTTP status codes.

Sensitive information (such as passwords) is never exposed in API responses.

For a detailed explanation of all changes, please refer to CHANGES.md.
