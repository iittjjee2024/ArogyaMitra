import random

class WorkoutModel:

    def __init__(self):
        self.workouts = {
            "beginner": [
                "Jumping Jacks",
                "Bodyweight Squats",
                "Push-ups",
                "Plank",
                "Walking Lunges"
            ],
            "intermediate": [
                "Burpees",
                "Pull-ups",
                "Dumbbell Bench Press",
                "Mountain Climbers",
                "Russian Twists"
            ],
            "advanced": [
                "Deadlifts",
                "Barbell Squats",
                "Handstand Push-ups",
                "Box Jumps",
                "Weighted Lunges"
            ]
        }

    def generate_workout_plan(self, level="beginner", days=5):

        if level not in self.workouts:
            level = "beginner"

        exercises = self.workouts[level]

        plan = []

        for day in range(1, days + 1):

            day_plan = {
                "day": day,
                "exercises": random.sample(exercises, 3)
            }

            plan.append(day_plan)

        return {
            "level": level,
            "days": days,
            "plan": plan
        }