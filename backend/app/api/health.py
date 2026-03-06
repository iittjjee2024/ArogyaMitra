from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.database import crud, schemas
from app.ai_models.health_prediction import HealthPredictionModel

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)

health_model = HealthPredictionModel()

@router.get("/bmi")
def calculate_bmi(weight: float, height: float):

    if weight <= 0 or height <= 0:
        raise HTTPException(status_code=400, detail="Invalid weight or height")

    bmi = health_model.calculate_bmi(weight, height)

    category = health_model.bmi_category(bmi)

    return {
        "weight": weight,
        "height": height,
        "bmi": bmi,
        "category": category
    }
@router.post("/predict")
def predict_health(
    weight: float,
    height: float,
    activity_level: str = "medium"
):

    result = health_model.predict(weight, height, activity_level)

    return result

@router.post("/record")
def save_health_record(
    record: schemas.HealthCreate,
    db: Session = Depends(get_db)
):

    saved = crud.create_health_record(db, record)

    return {
        "message": "Health record saved",
        "data": saved
    }

@router.get("/records/{user_id}")
def get_health_records(
    user_id: int,
    db: Session = Depends(get_db)
):

    records = crud.get_health_records(db, user_id)

    if not records:
        raise HTTPException(status_code=404, detail="No health records found")

    return records