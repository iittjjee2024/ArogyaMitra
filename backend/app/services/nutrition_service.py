import requests
from typing import List, Dict, Any
from app.core.config import settings

SPOONACULAR_BASE_URL = "https://api.spoonacular.com"
API_KEY = settings.SPOONACULAR_API_KEY


class NutritionService:
    def search_recipes(self, query: str, number: int = 10) -> Dict:

        url = f"{SPOONACULAR_BASE_URL}/recipes/complexSearch"

        params = {
            "query": query,
            "number": number,
            "addRecipeInformation": True,
            "apiKey": API_KEY
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:
            return {"error": "Failed to fetch recipes"}

        return response.json()

    def get_recipe_details(self, recipe_id: int) -> Dict:

        url = f"{SPOONACULAR_BASE_URL}/recipes/{recipe_id}/information"

        params = {
            "includeNutrition": True,
            "apiKey": API_KEY
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:
            return {"error": "Recipe not found"}

        return response.json()

    def get_recipe_nutrition(self, recipe_id: int) -> Dict:

        url = f"{SPOONACULAR_BASE_URL}/recipes/{recipe_id}/nutritionWidget.json"

        params = {
            "apiKey": API_KEY
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:
            return {"error": "Nutrition data not available"}

        return response.json()

    def generate_meal_plan(self, calories: int = 2000, diet: str = None):

        url = f"{SPOONACULAR_BASE_URL}/mealplanner/generate"

        params = {
            "timeFrame": "day",
            "targetCalories": calories,
            "diet": diet,
            "apiKey": API_KEY
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:
            return {"error": "Meal plan generation failed"}

        return response.json()

    def calculate_calories(self, age: int, weight: float, height: float, gender: str):

        if gender.lower() == "male":
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161

        return {
            "BMR": round(bmr, 2),
            "maintenance_calories": round(bmr * 1.2, 2),
            "weight_loss_calories": round(bmr * 0.85, 2),
            "weight_gain_calories": round(bmr * 1.3, 2)
        }
    def recommend_diet(self, health_goal: str):

        recommendations = {
            "weight_loss": [
                "Grilled Chicken Salad",
                "Quinoa Bowl",
                "Vegetable Soup"
            ],
            "muscle_gain": [
                "Protein Smoothie",
                "Chicken Breast with Brown Rice",
                "Egg Omelette"
            ],
            "diabetes": [
                "Low Carb Salad",
                "Oats with Almond Milk",
                "Steamed Vegetables"
            ],
            "heart_health": [
                "Salmon with Avocado",
                "Olive Oil Salad",
                "Whole Grain Toast"
            ]
        }

        return recommendations.get(health_goal.lower(), [])

    def ai_nutrition_coach(self, user_goal: str, weight: float, diet_type: str):

        try:

            from groq import Groq

            client = Groq(api_key=settings.GROQ_API_KEY)

            prompt = f"""
            Create a healthy meal recommendation.

            Goal: {user_goal}
            Weight: {weight} kg
            Diet type: {diet_type}

            Provide breakfast, lunch, dinner and snack recommendations.
            """

            chat = client.chat.completions.create(
                messages=[
                    {"role": "user", "content": prompt}
                ],
                model="llama3-70b-8192"
            )

            return {
                "ai_recommendation": chat.choices[0].message.content
            }

        except Exception as e:

            return {
                "error": str(e)
            }

nutrition_service = NutritionService()
