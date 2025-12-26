import os
import pandas as pd
import onnxruntime as ort
import numpy as np

os.makedirs("./outputs", exist_ok=True)

df = pd.read_csv("./data/processed/sensor_data_clean.csv")
X = df[["Humidity", "TimeIndex"]].values.astype(np.float32)

session = ort.InferenceSession("./models/temperature_model.onnx")
input_name = session.get_inputs()[0].name

predictions = session.run(None, {input_name: X})[0].ravel()
df["Predicted_Temperature"] = predictions

df.to_csv("./outputs/predictions.csv", index=False)
print("Predictions generated using ONNX model.")
