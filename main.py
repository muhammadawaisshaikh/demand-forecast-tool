from fastapi import FastAPI
from api.sales_prediction.sales_prediction import router as sales_prediction_router

app = FastAPI(
    title="Ai Forecasting for Sales & Demand",
    description="Provides insights and predictions based on sales data exported from SAP or similar systems.",
    version="1.0.0"
)

# Register all routers
app.include_router(sales_prediction_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
