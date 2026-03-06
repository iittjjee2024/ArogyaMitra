# ArogyaMitra API Documentation

## Base URL

http://localhost:8000

Production Example

https://api.arogyamitra.ai

---

# Authentication

All protected endpoints require a JWT token.

Header Example:

Authorization: Bearer <access_token>

---

# Auth APIs

## Register User

POST /auth/register

Request Body

{
  "email": "user@gmail.com",
  "password": "StrongPassword123",
  "age": 25,
  "weight": 70,
  "height": 175
}

Response

{
  "message": "User registered successfully"
}

---

## Login

POST /auth/login

Request

{
  "email": "user@gmail.com",
  "password": "StrongPassword123"
}

Response

{
  "access_token": "jwt_token_here",
  "token_type": "bearer"
}

---

# User APIs

## Get Profile

GET /users/profile

Response

{
  "email": "user@gmail.com",
  "age": 25,
  "weight": 70,
  "height": 175
}

---

## Update Profile

PUT /users/profile

Request

{
  "age": 26,
  "weight": 72
}

---

# Workout APIs

## Get Workout Plan

GET /workout/plan

Response

{
  "goal": "weight_loss",
  "plan": [
    {
      "exercise": "Push-ups",
      "sets": 3,
      "reps": 12
    }
  ]
}

---

# Nutrition APIs

## Get Diet Plan

GET /nutrition/plan

Response

{
  "calories": 2200,
  "meals": [
    {
      "meal": "Breakfast",
      "items": ["Oats", "Eggs"]
    }
  ]
}

---

# Health Prediction

POST /health/predict

Request

{
  "age": 40,
  "bmi": 29,
  "blood_pressure": 140
}

Response

{
  "risk": "Moderate",
  "recommendations": [
    "Exercise daily",
    "Reduce sodium intake"
  ]
}

---

# Admin APIs

## Get All Users

GET /admin/users

## Get System Stats

GET /admin/stats

Response

{
  "total_users": 1250,
  "active_today": 215
}
