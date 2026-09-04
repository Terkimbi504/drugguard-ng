#!/usr/bin/env python3
"""
Initialize DrugGuard NG project
Generates dataset, trains model, and initializes database
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(command, description):
    """Run a command and print status"""
    print(f"\n{'='*50}")
    print(f"  {description}")
    print(f"{'='*50}")
    try:
        result = subprocess.run(command, shell=True, check=True)
        print(f"✅ {description} - SUCCESS")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - FAILED")
        return False

def main():
    print("\n" + "="*50)
    print("  DrugGuard NG - Initialization Script")
    print("="*50)

    # Change to project root
    project_root = Path(__file__).parent
    os.chdir(project_root)

    # 1. Generate dataset
    success = run_command(
        f"{sys.executable} generate_dataset.py",
        "Generate Demo Dataset"
    )
    
    if not success:
        print("Failed to generate dataset. Continuing anyway...")

    # 2. Install backend dependencies
    success = run_command(
        f"{sys.executable} -m pip install -r backend/requirements.txt",
        "Install Backend Dependencies"
    )
    
    if not success:
        print("Warning: Some dependencies may not be installed")

    # 3. Train model
    success = run_command(
        f"{sys.executable} backend/app/ml/train_model.py",
        "Train ML Model"
    )
    
    if not success:
        print("Warning: Model training may have issues")

    # 4. Run tests
    success = run_command(
        f"{sys.executable} -m pytest backend/tests/ -v",
        "Run Backend Tests"
    )

    # 5. Summary
    print("\n" + "="*50)
    print("  ✅ Initialization Complete!")
    print("="*50)
    print("\nNext steps:")
    print("1. Start backend: uvicorn backend.app.main:app --reload")
    print("2. Start frontend: cd frontend && npm install && npm run dev")
    print("3. Visit http://localhost:5173")

if __name__ == "__main__":
    main()
