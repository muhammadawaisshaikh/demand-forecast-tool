from fastapi import APIRouter
from .schema import SalesPredictionInput
from .model import train_and_predict

router = APIRouter(
    prefix="/api/sales-prediction-ml",
    tags=["ML Sales Prediction"]
)

@router.get("/")
def get_info():
    return {"message": "ML-based sales prediction endpoint"}

@router.post("/sales-prediction-ml")
def predict_sales(data: SalesPredictionInput):
    prediction = train_and_predict([s.dict() for s in data.SalesOrderReport])
    return {
        "predictions": prediction,
        "constraints": {
            "min_data_points": 2,
            "grouped_by": "Material",
            "target": "Quantity",
            "model": "LinearRegression"
        }
    }
