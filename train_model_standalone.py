"""Machine Learning Model Training - Complete Implementation"""
import sys
import os
from pathlib import Path

def train_model():
    """Train the ML model"""
    try:
        import pandas as pd
        from sklearn.model_selection import train_test_split
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
        import joblib
        
        # Load data
        data_path = Path(__file__).parent.parent.parent / "data" / "products.csv"
        
        if not data_path.exists():
            print(f"Error: Dataset not found at {data_path}")
            return False
        
        print(f"Loading data from {data_path}")
        df = pd.read_csv(data_path)
        print(f"✓ Loaded {len(df)} records")
        
        # Prepare features
        features = [
            'nafdac_registered',
            'manufacturer_verified',
            'registration_valid',
            'barcode_verified',
            'batch_verified',
            'expiry_valid',
            'packaging_match',
            'distributor_verified',
            'price_anomaly'
        ]
        
        X = df[features].astype(int)
        y = df['genuine'].astype(int)
        
        print(f"✓ Features: {len(features)}")
        print(f"✓ Genuine products: {y.sum()}")
        print(f"✓ Suspicious products: {len(y) - y.sum()}")
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        print(f"✓ Training set: {len(X_train)}, Test set: {len(X_test)}")
        
        # Train Random Forest
        print("\nTraining Random Forest Classifier...")
        model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            random_state=42,
            class_weight='balanced'
        )
        model.fit(X_train, y_train)
        
        # Evaluate
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, zero_division=0)
        recall = recall_score(y_test, y_pred, zero_division=0)
        f1 = f1_score(y_test, y_pred, zero_division=0)
        
        print(f"✓ Accuracy:  {accuracy:.4f}")
        print(f"✓ Precision: {precision:.4f}")
        print(f"✓ Recall:    {recall:.4f}")
        print(f"✓ F1 Score:  {f1:.4f}")
        
        # Save model
        model_path = Path(__file__).parent / "model.joblib"
        os.makedirs(model_path.parent, exist_ok=True)
        
        model_data = {
            'model': model,
            'features': features,
            'model_name': 'Random Forest'
        }
        joblib.dump(model_data, str(model_path))
        print(f"\n✅ Model saved to {model_path}")
        
        return True
        
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Install with: pip install pandas scikit-learn joblib")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = train_model()
    sys.exit(0 if success else 1)
