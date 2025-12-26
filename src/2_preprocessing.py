import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

os.makedirs("./data/processed", exist_ok=True)

df = pd.read_csv("./data/raw/sensor_data_raw.csv")
df.interpolate(inplace=True)

df["TimeIndex"] = range(len(df))

feature_cols = ["Humidity", "TimeIndex"]
scaler = StandardScaler()
df[feature_cols] = scaler.fit_transform(df[feature_cols])

df.to_csv("./data/processed/sensor_data_clean.csv", index=False)
print("Data cleaned and features scaled.")
