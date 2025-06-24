from fastapi import APIRouter
from collections import defaultdict
from datetime import datetime

from models.models import SalesRequest

router = APIRouter(
    prefix="/api",
    tags=["Naive based Sales Prediction"]
)

@router.get("/")
def get_info():
    return {"message": "Naive-based sales prediction endpoint"}

@router.post("/sales-prediction-naive")
async def analyze_sales(data: SalesRequest):
    product_sales = defaultdict(list)

    for sale in data.SalesOrderReport:
        if sale.Status in ["Open", "Confirmed", "Delivered"]:
            product_sales[sale.Material].append(sale)

    results = []
    for product in data.SE16N_MARA:
        matnr = product.MATNR
        sales = product_sales.get(matnr, [])
        
        if not sales:
            continue

        total_quantity = sum(s.Quantity for s in sales)
        total_value = sum(s.NetValue for s in sales)
        earliest = min(datetime.fromisoformat(s.DeliveryDate) for s in sales)
        latest = max(datetime.fromisoformat(s.DeliveryDate) for s in sales)
        months_range = max(1, ((latest - earliest).days) // 30)

        predicted_monthly_sales = total_quantity / months_range
        predicted_next_quarter = predicted_monthly_sales * 3

        results.append({
            "MaterialNumber": matnr,
            "MaterialType": product.MTART,
            "Unit": product.MEINS,
            "TotalSalesQuantity": total_quantity,
            "TotalNetValue": round(total_value, 2),
            "AvgMonthlySales": round(predicted_monthly_sales, 2),
            "ForecastNextQuarter": round(predicted_next_quarter, 2),
            "KeyConstraints": {
                "Plant": product.WERKS,
                "CompanyCode": product.BUKRS,
                "ProductGroup": product.MATKL,
                "Division": product.SPART,
                "StatusConsidered": ["Open", "Confirmed", "Delivered"]
            }
        })

    return {
        "summary": {
            "totalProducts": len(results),
            "averageForecastedSalesNextQuarter": round(
                sum(r["ForecastNextQuarter"] for r in results) / len(results), 2
            ) if results else 0
        },
        "products": results
    }
