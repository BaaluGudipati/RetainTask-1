When I got the code, it was working but had serious real-world risks. So I focused on fixing the biggest problems first, while keeping the project simple and functional.

The Critical Issues I Fixed:

1️⃣ Passwords Were Stored in Plaintext (Critical Security Flaw)
Original code was storing raw passwords in the database.

I fixed this by hashing passwords using PBKDF2-SHA256 before storing them.

Also, during login, I securely verify the password using hash comparison instead of direct string matching.

2️⃣ SQL Injection Vulnerability
The app was building SQL queries using f-strings, which is dangerous.

I replaced all of them with safe parameterized queries to prevent SQL Injection attacks.

3️⃣ Code Was All In One Big File (No Separation of Concerns)
All the DB code, route handling, and business logic were mixed together.

I reorganized the codebase into a clean structure:

/models → Handles DB queries.

/routes → Handles API endpoints.

/utils → Helper functions for authentication and validation.

4️⃣ Database Connection Handling Was Unsafe
The code was using a global SQLite connection shared by all API requests.

I refactored it to create a new DB connection per request, making it safe for multiple users hitting the API.

5️⃣ No Input Validation
Incoming request data wasn’t being checked — anyone could send bad/malicious data.

I added basic input validation to ensure required fields are present and valid before proceeding.

6️⃣ Inconsistent API Responses & Status Codes
API was returning plain text responses with no proper status codes.

I standardized all responses to be structured JSON and return correct HTTP status codes (200, 201, 400, 404).

7️⃣ Sensitive Data (Passwords) Were Being Returned in API Responses
Originally, when fetching user data, the password field was also returned.

I fixed this by ensuring sensitive fields like passwords are never sent in API responses.

🗂️ Why I Didn't Add DB Environments or Cloud DBs
Since the app uses SQLite (a local file-based DB), there’s no need for external DB environments.

I didn’t add environment variables for DB configs because the SQLite DB path is static and local.

Setting up a cloud database or full environment config would have been unnecessary for this assignment.

The focus was on fixing code-level issues, not infrastructure deployment.

🎯 My Approach & Focus:
Fix real-world security risks first (Passwords, SQL Injection).

Make the code organized and maintainable.

Ensure API remains fully functional after refactor.


I didn’t over-engineer — I kept it simple and solved the problems that matter in a real production scenario.
