import random

class NutritionModel:

    def __init__(self):

        self.meals = {
            "breakfast": [
                "Oatmeal with fruits",
                "Egg omelette",
                "Greek yogurt with nuts",
                "Avocado toast"
            ],
            "lunch": [
                "Grilled chicken salad",
                "Quinoa vegetable bowl",
                "Brown rice with tofu",
                "Vegetable soup"
            ],
            "dinner": [
                "Grilled fish with vegetables",
                "Chicken stir fry",
                "Paneer salad",
                "Lentil soup"
            ]
        }

    def generate_meal_plan(self, days=7):

        plan = []

        for day in range(1, days + 1):

            day_meal = {
                "day": day,
                "breakfast": random.choice(self.meals["breakfast"]),
                "lunch": random.choice(self.meals["lunch"]),
                "dinner": random.choice(self.meals["dinner"])
            }

            plan.append(day_meal)

        return {
            "days": days,
            "meal_plan": plan
        }