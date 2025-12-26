# Advanced IoT Data Pipeline

## Project Overview
This project demonstrates a complete **end-to-end IoT data pipeline** using Python. It covers data acquisition, preprocessing, machine learning model training, ONNX export, prediction, and evaluation with visualization.

The pipeline can handle both **synthetic** and **real-world sensor data** (temperature, humidity, air quality, etc.), making it a versatile example for IoT and data science projects.

---

## Project Structure

final_project/
│
├── data/
│ ├── raw/ # Raw sensor datasets (synthetic or downloaded)
│ └── processed/ # Cleaned and preprocessed data
│
├── models/ # Trained ML model in ONNX format
│ └── temperature_model.onnx
│
├── outputs/
│ ├── plots/ # Visualizations (actual vs predicted, error plots)
│ └── predictions.csv # Model predictions
│
├── src/ # Python scripts for each pipeline step
│ ├── 1_data_acquisition.py
│ ├── 2_preprocessing.py
│ ├── 3_train_and_export_onnx.py
│ ├── 4_load_and_predict.py
│ └── 5_evaluation.py
│
├── all_in_one.py # Optional: Run the full pipeline in a single script
└── requirements.txt # Required Python packages

markdown
Copy code

---

## Features

- **Data Acquisition**
  - Generate synthetic sensor data (temperature, humidity, etc.)
  - Download real datasets (Weather, Air Quality, Smart Home)
  - Simulate noise and missing values to mimic real IoT streams

- **Data Preprocessing**
  - Handle missing or corrupted values
  - Normalize and scale features
  - Smooth time-series data
  - Feature selection and train-test split

- **Machine Learning**
  - Train regression or classification models
  - Export models to **ONNX** for cross-platform compatibility

- **Prediction & Evaluation**
  - Load ONNX model with `onnxruntime`
  - Generate predictions on real or test sensor data
  - Evaluate model performance using metrics
  - Plot actual vs predicted values and errors

---

## Installation

1. Clone the repository:
```bash
git clone <repository_url>
cd final_project
Create a virtual environment and install dependencies:

bash
Copy code
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
Usage
Run individual scripts step-by-step:

bash
Copy code
python src/1_data_acquisition.py
python src/2_preprocessing.py
python src/3_train_and_export_onnx.py
python src/4_load_and_predict.py
python src/5_evaluation.py
Or run the full pipeline with:

bash
Copy code
python all_in_one.py
Check outputs:

Cleaned data: data/processed/

Predictions: outputs/predictions.csv

Visualizations: outputs/plots/

Requirements
Python 3.8+

pandas, numpy, scikit-learn

skl2onnx, onnxruntime

matplotlib, seaborn

(Install all via pip install -r requirements.txt)

Author
Elika Bagheri
Advanced Computer Programming Project
2025
