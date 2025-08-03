import re

def is_valid_email(email):
    """Validate email format using regex."""
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

def is_valid_password(password):
    """Ensure password has at least 6 characters."""
    return len(password) >= 6
