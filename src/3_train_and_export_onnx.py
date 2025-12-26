import os
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

os.makedirs("./models", exist_ok=True)

df = pd.read_csv("./data/processed/sensor_data_clean.csv")

X = df[["Humidity", "TimeIndex"]].values
y = df["Temperature"].values  

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

initial_type = [('float_input', FloatTensorType([None, 2]))]
onnx_model = convert_sklearn(model, initial_types=initial_type)

with open("./models/temperature_model.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())

print("Model trained and exported to ONNX.")
