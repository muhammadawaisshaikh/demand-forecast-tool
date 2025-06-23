from pydantic import BaseModel
from typing import List


class SalesOrder(BaseModel):
    SalesOrder: str
    Customer: str
    Material: str
    Quantity: int
    NetValue: float
    Currency: str
    DeliveryDate: str
    Status: str


class Material(BaseModel):
    MATNR: str
    WERKS: str
    BUKRS: str
    MATKL: str
    MEINS: str
    MTART: str
    MBRSH: str
    SPART: str


class SalesRequest(BaseModel):
    SE16N_MARA: List[Material]
    SalesOrderReport: List[SalesOrder]
