User Management API – Refactored & Refined
A sleek, secure, and fully-documented rewrite of the legacy user-management service. Clean architecture, hardened security, and zero breaking changes.

Getting Started
1. Prerequisites
   - Python 3.8+
   - SQLite3 (bundled with Python)
   - pip
2. One-line Launch
   pip install -r requirements.txt && python init_db.py && python app.py
   API spins up at → http://localhost:5009

Endpoints
GET  /                 Health Check
GET  /users            Get all users
GET  /user/<id>        Get user by ID
POST /users            Create new user
PUT  /user/<id>        Update user details
DELETE /user/<id>      Delete user
GET  /search?name=<n>  Search users by name
POST /login            User login

Project Tree
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

Key Improvements
- Passwords hashed with PBKDF2-SHA256 (no plaintext ever)
- Parameterized queries eliminate SQL injection
- Modular codebase: routes, models, utilities separated
- Per-request DB connections for thread safety
- Robust input validation on create/update/login
- Standardized JSON responses & correct HTTP codes
- Sensitive data never exposed in responses
