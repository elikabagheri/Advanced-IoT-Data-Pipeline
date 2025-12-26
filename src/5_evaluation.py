import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

os.makedirs("./outputs/plots", exist_ok=True)

df = pd.read_csv("./outputs/predictions.csv")

mse = mean_squared_error(df["Temperature"], df["Predicted_Temperature"])
print("MSE:", mse)

plt.figure(figsize=(10, 4))
plt.plot(df["Temperature"], label="Actual")
plt.plot(df["Predicted_Temperature"], label="Predicted")
plt.legend()
plt.title("Actual vs Predicted Temperature")
plt.savefig("./outputs/plots/actual_vs_pred.png")

plt.figure(figsize=(10, 4))
plt.plot(df["Temperature"] - df["Predicted_Temperature"])
plt.title("Prediction Error")
plt.savefig("./outputs/plots/error_plot.png")
