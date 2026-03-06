import random

class AIHealthCoach:

    def generate_workout(self, weight, goal):

        workouts = [
            "Pushups",
            "Squats",
            "Running",
            "Cycling",
            "Yoga"
        ]

        return {
            "goal": goal,
            "recommended_workout": random.choice(workouts)
        }

    def generate_diet(self, weight):

        meals = [
            "High Protein Diet",
            "Balanced Diet",
            "Low Carb Diet"
        ]

        return random.choice(meals)

coach = AIHealthCoach()
