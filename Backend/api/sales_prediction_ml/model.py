from sklearn.linear_model import LinearRegression
import numpy as np
from typing import List, Tuple
import pandas as pd

def train_and_predict(sales_data: List[dict], predict_steps: int = 1) -> Tuple[float, float]:
    df = pd.DataFrame(sales_data)

    # Group by material to predict per material
    results = []
    for material, group in df.groupby("Material"):
        group = group.sort_values(by="DeliveryDate")
        group["index"] = np.arange(len(group))
        X = group[["index"]]
        y = group["Quantity"]

        if len(X) < 2:
            continue  # skip insufficient data

        model = LinearRegression()
        model.fit(X, y)

        future_index = np.array([[len(X) + i] for i in range(predict_steps)])
        y_pred = model.predict(future_index)

        results.append({
            "Material": material,
            "PredictedNextQuantity": round(y_pred[-1], 2),
            "AverageHistoricalQuantity": round(y.mean(), 2),
            "SellThroughRate": round(y.sum() / len(y), 2)
        })

    return results
