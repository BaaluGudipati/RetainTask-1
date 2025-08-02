# 🛡️ User Management API — Refactored & Secure

A **clean, secure, and production-ready** refactor of the legacy User Management API.  
This project focuses on fixing **critical security flaws**, restructuring the codebase into a **modular architecture**, and ensuring **zero breaking changes** to existing endpoints.

---

## ✨ Key Improvements

- 🔐 **Passwords hashed** with PBKDF2-SHA256 (no plaintext storage)
- 🛡️ **SQL Injection vulnerabilities fixed** with parameterized queries
- 🗂️ **Modular codebase** — Clean separation of routes, models, utilities
- 🧵 **Per-request DB connections** ensuring thread-safety
- 📋 **Robust input validation** on create, update, and login operations
- 📊 **Standardized JSON responses** with correct HTTP status codes
- 🚫 **Sensitive data like passwords never exposed** in API responses

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

