import uuid
import random
from datetime import datetime

def generate_id():
    return str(uuid.uuid4())

def get_timestamp():
    return datetime.utcnow().isoformat()

def calculate_bmi(weight, height):
    """
    weight in kg
    height in cm
    """
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

def bmi_category(bmi):

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obese"

def random_items(items, count=3):

    if count > len(items):
        count = len(items)

    return random.sample(items, count)

def paginate(data, page=1, limit=10):

    start = (page - 1) * limit
    end = start + limit

    return {
        "page": page,
        "limit": limit,
        "total": len(data),
        "results": data[start:end]
    }
