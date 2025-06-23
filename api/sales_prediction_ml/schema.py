from pydantic import BaseModel
from typing import List

class SalesOrder(BaseModel):
    SalesOrder: str
    Customer: str
    Material: str
    Quantity: int
    NetValue: float
    Currency: str
    DeliveryDate: str  # For simplicity; can use datetime
    Status: str

class SalesPredictionInput(BaseModel):
    SalesOrderReport: List[SalesOrder]
