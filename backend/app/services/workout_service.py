"""
ArogyaMitra - Workout Service
--------------------------------
Generates personalized workout plans based on
user health conditions, BMI, and goals.

Author: ArogyaMitra AI System
"""

from typing import Dict, List
import random


class WorkoutService:

    def __init__(self):
        pass

    def calculate_bmi(self, weight: float, height: float) -> float:
        """
        Calculate Body Mass Index
        """
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        return round(bmi, 2)
    def bmi_category(self, bmi: float) -> str:

        if bmi < 18.5:
            return "underweight"

        elif 18.5 <= bmi < 25:
            return "normal"

        elif 25 <= bmi < 30:
            return "overweight"

        else:
            return "obese"

    WORKOUT_DB = {

        "weight_loss": [
            "Jump Rope",
            "Running",
            "Burpees",
            "Mountain Climbers",
            "Cycling",
            "HIIT Training",
            "Fast Walking",
            "Stair Climbing"
        ],

        "muscle_gain": [
            "Push-ups",
            "Pull-ups",
            "Bench Press",
            "Squats",
            "Deadlifts",
            "Dumbbell Rows",
            "Shoulder Press",
            "Plank"
        ],

        "general_fitness": [
            "Yoga",
            "Walking",
            "Stretching",
            "Light Jogging",
            "Pilates",
            "Bodyweight Squats",
            "Core Exercises"
        ],

        "diabetes": [
            "Brisk Walking",
            "Cycling",
            "Yoga",
            "Light Strength Training",
            "Swimming"
        ],

        "heart": [
            "Walking",
            "Stationary Cycling",
            "Light Yoga",
            "Breathing Exercises"
        ],

        "hypertension": [
            "Walking",
            "Yoga",
            "Meditation",
            "Light Cardio"
        ]
    }

    def recommend_by_bmi(self, bmi: float) -> List[str]:

        category = self.bmi_category(bmi)

        if category == "underweight":
            return random.sample(self.WORKOUT_DB["muscle_gain"], 4)

        elif category == "normal":
            return random.sample(self.WORKOUT_DB["general_fitness"], 4)

        elif category == "overweight":
            return random.sample(self.WORKOUT_DB["weight_loss"], 5)

        else:
            return random.sample(self.WORKOUT_DB["weight_loss"], 6)

    def recommend_by_condition(self, conditions: List[str]) -> List[str]:

        workouts = []

        for condition in conditions:

            if condition in self.WORKOUT_DB:
                workouts.extend(self.WORKOUT_DB[condition])

        return list(set(workouts))

    def generate_daily_plan(
        self,
        age: int,
        weight: float,
        height: float,
        conditions: List[str]
    ) -> Dict:

        bmi = self.calculate_bmi(weight, height)

        bmi_workouts = self.recommend_by_bmi(bmi)

        condition_workouts = self.recommend_by_condition(conditions)

        combined = list(set(bmi_workouts + condition_workouts))

        selected = random.sample(combined, min(5, len(combined)))

        return {
            "bmi": bmi,
            "category": self.bmi_category(bmi),
            "recommended_workouts": selected
        }
    def generate_weekly_plan(
        self,
        age: int,
        weight: float,
        height: float,
        conditions: List[str]
    ) -> Dict:

        days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]

        weekly_plan = {}

        for day in days:

            weekly_plan[day] = self.generate_daily_plan(
                age,
                weight,
                height,
                conditions
            )

        return weekly_plan


if __name__ == "__main__":

    service = WorkoutService()

    user_profile = {
        "age": 30,
        "weight": 78,
        "height": 175,
        "conditions": ["diabetes"]
    }

    daily_plan = service.generate_daily_plan(
        user_profile["age"],
        user_profile["weight"],
        user_profile["height"],
        user_profile["conditions"]
    )

    print("Daily Workout Plan")
    print(daily_plan)