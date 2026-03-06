import requests

BASE_URL = "http://127.0.0.1:8000"


def test_health():

    url = f"{BASE_URL}/health/bmi"

    params = {
        "weight": 70,
        "height": 175
    }

    response = requests.get(url, params=params)

    print("BMI API Response:")
    print(response.json())


def test_workout():

    url = f"{BASE_URL}/workouts/generate"

    response = requests.get(url)

    print("\nWorkout API Response:")
    print(response.json())


def test_nutrition():

    url = f"{BASE_URL}/nutrition/search"

    params = {"query": "pizza"}

    response = requests.get(url, params=params)

    print("\nNutrition API Response:")
    print(response.json())


if __name__ == "__main__":

    test_health()
    test_workout()
    test_nutrition()
    