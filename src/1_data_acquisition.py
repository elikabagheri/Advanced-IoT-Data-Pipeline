import os
import pandas as pd
import numpy as np

os.makedirs("./data/raw", exist_ok=True)

np.random.seed(42)
time = pd.date_range("2025-01-01", periods=500, freq="h")

temperature = 20 + 5*np.sin(np.linspace(0, 20, 500)) + np.random.normal(0, 0.8, 500)
humidity = 50 + 10*np.cos(np.linspace(0, 20, 500)) + np.random.normal(0, 1.5, 500)

df = pd.DataFrame({
    "Time": time,
    "Temperature": temperature,
    "Humidity": humidity
})

for col in ["Temperature", "Humidity"]:
    df.loc[df.sample(frac=0.05).index, col] = np.nan

df.to_csv("./data/raw/sensor_data_raw.csv", index=False)
print("Raw sensor data generated.")
