"""Module that contains common helpers that
will be using in the project"""

def validate_email(email: str) -> bool:
    """Validates email format"""
    import re
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email) is not None
