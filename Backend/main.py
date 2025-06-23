from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from api.sales_prediction_naive.sales_prediction import router as naive_router
from api.sales_prediction_ml.sales_prediction_ml import router as ml_router

app = FastAPI(
    title="AI Forecasting for Sales & Demand",
    description="Provides insights and predictions based on sales data exported from SAP or similar systems.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Api routers
app.include_router(naive_router)
app.include_router(ml_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
