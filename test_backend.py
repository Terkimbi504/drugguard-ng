#!/usr/bin/env python3
"""
Comprehensive test of DrugGuard NG backend
This script tests all major components without pytest
"""

import sys
from pathlib import Path

def print_header(text):
    print(f"\n{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}\n")

def test_imports():
    """Test that all required modules can be imported"""
    print_header("Testing Imports")
    
    try:
        print("✓ Checking FastAPI...")
        import fastapi
        print(f"  FastAPI version: {fastapi.__version__}")
    except ImportError as e:
        print(f"✗ FastAPI not found: {e}")
        return False
    
    try:
        print("✓ Checking Pandas...")
        import pandas
        print(f"  Pandas version: {pandas.__version__}")
    except ImportError:
        print("⚠ Pandas not installed (ML features will be limited)")
    
    try:
        print("✓ Checking SQLAlchemy...")
        import sqlalchemy
        print(f"  SQLAlchemy version: {sqlalchemy.__version__}")
    except ImportError as e:
        print(f"✗ SQLAlchemy not found: {e}")
        return False
    
    return True

def test_database():
    """Test database setup"""
    print_header("Testing Database Setup")
    
    sys.path.insert(0, str(Path(__file__).parent / "backend"))
    
    try:
        from app.database import init_db, SessionLocal
        from app.models import Product
        
        print("✓ Database imports successful")
        
        # Initialize database
        init_db()
        print("✓ Database initialized")
        
        # Test session
        db = SessionLocal()
        count = db.query(Product).count()
        db.close()
        print(f"✓ Database query successful (Products in DB: {count})")
        
        return True
    except Exception as e:
        print(f"✗ Database test failed: {e}")
        return False

def test_api():
    """Test API routes"""
    print_header("Testing API Routes")
    
    sys.path.insert(0, str(Path(__file__).parent / "backend"))
    
    try:
        from fastapi.testclient import TestClient
        from app.main import app
        
        client = TestClient(app)
        
        # Test health endpoint
        print("Testing GET /api/health...")
        response = client.get("/api/health")
        if response.status_code == 200:
            print(f"✓ Health check passed: {response.json()}")
        else:
            print(f"✗ Health check failed: {response.status_code}")
            return False
        
        # Test root endpoint
        print("\nTesting GET /...")
        response = client.get("/")
        if response.status_code == 200:
            print(f"✓ Root endpoint working")
        else:
            print(f"✗ Root endpoint failed: {response.status_code}")
            return False
        
        # Test products list
        print("\nTesting GET /api/products...")
        response = client.get("/api/products")
        if response.status_code == 200:
            products = response.json()
            print(f"✓ Products endpoint working ({len(products)} products)")
        else:
            print(f"✗ Products endpoint failed: {response.status_code}")
            return False
        
        return True
    except Exception as e:
        print(f"✗ API test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_data():
    """Test data loading"""
    print_header("Testing Data Loading")
    
    try:
        data_path = Path(__file__).parent / "backend" / "data" / "products.csv"
        
        if not data_path.exists():
            print(f"✗ Data file not found: {data_path}")
            return False
        
        print(f"✓ Data file found: {data_path}")
        
        try:
            import pandas as pd
            df = pd.read_csv(data_path)
            genuine_series = df['genuine'].fillna(False).astype(bool)
            print(f"✓ Data loaded successfully")
            print(f"  Total records: {len(df)}")
            print(f"  Genuine products: {int(genuine_series.sum())}")
            print(f"  Suspicious products: {int((~genuine_series).sum())}")
            return True
        except ImportError:
            print("⚠ Pandas not available, skipping detailed data analysis")
            return True
        except Exception as e:
            print(f"✗ Error loading data: {e}")
            return False
            
    except Exception as e:
        print(f"✗ Data test failed: {e}")
        return False

def test_services():
    """Test business logic services"""
    print_header("Testing Services")
    
    sys.path.insert(0, str(Path(__file__).parent / "backend"))
    
    try:
        from app.services import RiskService, ExplanationService
        from app.schemas import VerificationIndicator
        
        # Test risk scoring
        print("Testing Risk Service...")
        indicators = [
            VerificationIndicator(name="Registration", status=True, description="OK"),
            VerificationIndicator(name="Barcode", status=False, description="Failed"),
            VerificationIndicator(name="Expiry", status=True, description="OK"),
        ]
        
        score = RiskService.calculate_risk_score(indicators)
        level = RiskService.get_risk_level(score)
        print(f"✓ Risk calculation working")
        print(f"  Sample risk score: {score}/100")
        print(f"  Risk level: {level}")
        
        # Test explanation
        print("\nTesting Explanation Service...")
        explanation = ExplanationService.generate_explanation(
            indicators,
            "Suspicious",
            score,
            True
        )
        print(f"✓ Explanation generation working")
        
        return True
    except Exception as e:
        print(f"✗ Services test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all tests"""
    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + " "*58 + "║")
    print("║" + "  DrugGuard NG - Backend Verification Tests".center(58) + "║")
    print("║" + " "*58 + "║")
    print("╚" + "="*58 + "╝")
    
    results = []
    
    # Run tests
    results.append(("Imports", test_imports()))
    results.append(("Database", test_database()))
    results.append(("Data", test_data()))
    results.append(("Services", test_services()))
    results.append(("API", test_api()))
    
    # Summary
    print_header("Test Summary")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n✅ All tests passed! DrugGuard NG is ready to run!")
        print("\nNext steps:")
        print("1. Start backend: uvicorn backend.app.main:app --reload")
        print("2. Start frontend: cd frontend && npm run dev")
        print("3. Visit: http://localhost:5173")
        return 0
    else:
        print(f"\n⚠️ {total - passed} test(s) failed. Check output above for details.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
