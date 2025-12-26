import os
import subprocess
import sys

SRC_DIR = "src"  

steps = [
    "1_data_acquisition.py",
    "2_preprocessing.py",
    "3_train_and_export_onnx.py",
    "4_load_and_predict.py",
    "5_evaluation.py"
]

def run_step(step_file):
    step_path = os.path.join(SRC_DIR, step_file)
    print(f"\n🚀 Running {step_file} ...")
    subprocess.run([sys.executable, step_path], check=True)
    print(f"✅ Finished {step_file}")

def main():
    print("💻 Starting all-in-one IoT project pipeline...\n")
    
    os.makedirs("./data/raw", exist_ok=True)
    os.makedirs("./data/processed", exist_ok=True)
    os.makedirs("./models", exist_ok=True)
    os.makedirs("./outputs", exist_ok=True)
    os.makedirs("./outputs/plots", exist_ok=True)

    for step in steps:
        run_step(step)
    
    print("\n🎉 All steps completed successfully!")
    print("Check outputs in 'outputs' and models in 'models'.")

if __name__ == "__main__":
    main()
