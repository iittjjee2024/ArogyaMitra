"""
ArogyaMitra - Recommendation Engine
-----------------------------------
This service generates personalized food recommendations
based on health conditions, nutrition requirements, and
user preferences.

Author: ArogyaMitra AI System
"""

import os
import requests
import random
from typing import List, Dict
from dotenv import load_dotenv

from services.nutrition_service import NutritionService

load_dotenv()

SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")
BASE_URL = "https://api.spoonacular.com/recipes/complexSearch"


class RecommendationEngine:
    """
    AI based food recommendation engine
    """

    def __init__(self):
        self.nutrition_service = NutritionService()

    HEALTH_RULES = {
        "diabetes": {
            "exclude": ["sugar", "honey", "cake", "cookies"],
            "diet": "low-carb"
        },
        "heart": {
            "exclude": ["butter", "bacon", "fried"],
            "diet": "low-fat"
        },
        "obesity": {
            "exclude": ["cheese", "cream"],
            "diet": "low-calorie"
        },
        "hypertension": {
            "exclude": ["salt", "processed"],
            "diet": "low-sodium"
        }
    }
    def fetch_recipes(self, query: str = "healthy", number: int = 10) -> List[Dict]:
        """
        Fetch recipes from Spoonacular API
        """

        params = {
            "query": query,
            "number": number,
            "apiKey": SPOONACULAR_API_KEY
        }

        response = requests.get(BASE_URL, params=params)

        if response.status_code != 200:
            raise Exception("Recipe API request failed")

        data = response.json()

        return data.get("results", [])

    def filter_by_health(self, recipes: List[Dict], conditions: List[str]) -> List[Dict]:
        """
        Filter recipes based on health conditions
        """

        filtered = []

        for recipe in recipes:

            title = recipe.get("title", "").lower()

            blocked = False

            for condition in conditions:

                rules = self.HEALTH_RULES.get(condition)

                if not rules:
                    continue

                for word in rules["exclude"]:
                    if word in title:
                        blocked = True

            if not blocked:
                filtered.append(recipe)

        return filtered

    def recommend_for_user(
        self,
        age: int,
        weight: float,
        height: float,
        conditions: List[str],
        preference: str = "vegetarian"
    ) -> Dict:
        """
        Generate personalized meal recommendation
        """

        nutrition = self.nutrition_service.calculate_daily_needs(
            age=age,
            weight=weight,
            height=height
        )
        recipes = self.fetch_recipes()
        healthy_recipes = self.filter_by_health(recipes, conditions)

        recommendations = random.sample(
            healthy_recipes,
            min(5, len(healthy_recipes))
        )

        return {
            "nutrition_requirements": nutrition,
            "recommended_meals": recommendations
        }

    def generate_daily_meal_plan(self, conditions: List[str]) -> Dict:
        """
        Generate breakfast, lunch, dinner plan
        """

        breakfast = self.fetch_recipes("healthy breakfast", 5)
        lunch = self.fetch_recipes("healthy lunch", 5)
        dinner = self.fetch_recipes("healthy dinner", 5)

        breakfast = self.filter_by_health(breakfast, conditions)
        lunch = self.filter_by_health(lunch, conditions)
        dinner = self.filter_by_health(dinner, conditions)

        return {

            "breakfast": random.choice(breakfast) if breakfast else None,
            "lunch": random.choice(lunch) if lunch else None,
            "dinner": random.choice(dinner) if dinner else None

        }

    def generate_weekly_plan(self, conditions: List[str]) -> Dict:
        """
        Generate 7-day healthy meal plan
        """

        days = [
            "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"
        ]

        weekly_plan = {}

        for day in days:

            weekly_plan[day] = self.generate_daily_meal_plan(conditions)

        return weekly_plan

if __name__ == "__main__":

    engine = RecommendationEngine()

    user_profile = {
        "age": 30,
        "weight": 70,
        "height": 170,
        "conditions": ["diabetes"]
    }

    recommendations = engine.recommend_for_user(
        age=user_profile["age"],
        weight=user_profile["weight"],
        height=user_profile["height"],
        conditions=user_profile["conditions"]
    )

    print("Recommended Meals")
    print(recommendations)
