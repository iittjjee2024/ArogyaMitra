import re
def validate_email(email: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

def validate_password(password: str) -> bool:
    """
    Password Rules
    - Minimum 8 characters
    - At least 1 uppercase
    - At least 1 lowercase
    - At least 1 number
    """

    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"[0-9]", password):
        return False

    return True

def validate_age(age: int) -> bool:

    if age < 5 or age > 120:
        return False

    return True

def validate_height(height: float) -> bool:

    if height < 50 or height > 300:
        return False

    return True

def validate_weight(weight: float) -> bool:

    if weight < 10 or weight > 500:
        return False

    return True

def validate_username(username: str) -> bool:

    if len(username) < 3:
        return False

    if not username.isalnum():
        return False

    return True