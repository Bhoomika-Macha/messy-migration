# CHANGES.md

## 🐞 Major Issues Identified in Legacy Code

- All logic bundled into one file (`app.py`)
- Vulnerable to SQL injection via string-formatted SQL queries
- Plain-text password storage (no hashing)
- No input validation (email, password)
- No use of Flask Blueprints or modular structure
- No unit tests or automated validation
- Responses returned as raw strings instead of JSON
- Repeated code and poor maintainability

---

## ✅ Refactoring Changes Made

- Introduced Flask **Blueprints** and **modular folder structure**
- Moved database logic to **SQLAlchemy models** (`models.py`)
- Implemented **input validation** (email format, password length)
- Used `werkzeug.security` for **password hashing and checking**
- Added proper **HTTP status codes** and JSON responses
- Refactored to follow **Flask app factory** pattern using `app.py` as the entry point
- Wrote **unit tests** for `/`, `/users`, and `/login`
- Used in-memory database (`sqlite:///:memory:`) for testing

---

## 🔧 Tools & Libraries Used

- Python 3.12
- Flask 2.3.2
- Flask-SQLAlchemy
- unittest (for tests)
- Werkzeug (for secure password handling)

---

## 🤖 AI Usage Acknowledgement

- Used **ChatGPT** as a coding assistant to:
  - Strategically plan the refactor based on the legacy code’s design issues.
  - Review Flask architectural patterns (e.g., app factory, Blueprints).
  - Reference best practices for password security and REST API design.
  - Speed up development of validation functions and test structure.

> All suggestions were independently validated, adapted, and manually implemented.  
> AI was used responsibly as a supportive tool, not a replacement for original work or understanding.

---

## ⏭️ What I Would Do With More Time

- Add **JWT-based authentication** for `/login`
- Use **environment variables** for secrets (via `python-dotenv`)
- Add **pagination** and **filtering** to `/users`
- Add **rate limiting** or request throttling
- Improve error messages using custom exceptions
- Set up **GitHub Actions** for automated tests
- Add **Swagger/OpenAPI** documentation
