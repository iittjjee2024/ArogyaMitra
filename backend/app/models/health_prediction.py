class HealthPredictionModel:

    def calculate_bmi(self, weight, height):

        height_m = height / 100
        bmi = weight / (height_m ** 2)

        return round(bmi, 2)

    def bmi_category(self, bmi):

        if bmi < 18.5:
            return "Underweight"

        elif bmi < 25:
            return "Normal"

        elif bmi < 30:
            return "Overweight"

        else:
            return "Obese"

    def health_risk(self, bmi, activity_level):

        if bmi > 30 and activity_level == "low":
            return "High Risk"

        if bmi > 25:
            return "Moderate Risk"

        return "Low Risk"

    def predict(self, weight, height, activity_level="medium"):

        bmi = self.calculate_bmi(weight, height)

        category = self.bmi_category(bmi)

        risk = self.health_risk(bmi, activity_level)

        return {
            "bmi": bmi,
            "category": category,
            "risk": risk
        }