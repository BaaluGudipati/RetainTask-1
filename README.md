#  User Management API — Refactored & Secure


---

##  Key Improvements

-  **Passwords hashed** with PBKDF2-SHA256 (no plaintext storage)
- **SQL Injection vulnerabilities fixed** with parameterized queries
- **Modular codebase** — Clean separation of routes, models, utilities
- **Per-request DB connections** ensuring thread-safety
- **Robust input validation** on create, update, and login operations
- **Standardized JSON responses** with correct HTTP status codes
- **Sensitive data like passwords never exposed** in API responses

---

## 🖥️ API Endpoints

| Method | Endpoint                | Description              |
|--------|-------------------------|--------------------------|
| GET    | `/`                     | Health Check              |
| GET    | `/users`                | Get all users             |
| GET    | `/user/<id>`            | Get user by ID            |
| POST   | `/users`                | Create new user           |
| PUT    | `/user/<id>`            | Update user details       |
| DELETE | `/user/<id>`            | Delete user               |
| GET    | `/search?name=<name>`   | Search users by name      |
| POST   | `/login`                | User login                |

---

## 🗂️ Folder Structure

```bash
messy-migration/
├── app.py
├── init_db.py
├── requirements.txt
├── CHANGES.md
├── README.md
├── models/
│ └── user_model.py
├── routes/
│ └── user_routes.py
└── utils/
├── auth.py
└── validators.py

