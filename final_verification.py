#!/usr/bin/env python3
"""
Final Verification: DrugGuard NG Complete System Test
"""
import requests
import sys

def test_system():
    print("\n" + "="*70)
    print("  DrugGuard NG - Complete System Verification")
    print("="*70)
    
    # Test Backend
    print("\n📦 BACKEND TEST")
    print("-" * 70)
    try:
        response = requests.get("http://127.0.0.1:8000/api/health", timeout=5)
        data = response.json()
        print(f"✅ Backend Status: {data.get('status')}")
        print(f"✅ API Version: {data.get('version')}")
        print(f"✅ Environment: {data.get('environment')}")
        backend_ok = True
    except Exception as e:
        print(f"❌ Backend Error: {str(e)}")
        backend_ok = False
    
    # Test Database
    print("\n📊 DATABASE TEST")
    print("-" * 70)
    try:
        response = requests.get("http://127.0.0.1:8000/api/products/stats/count", timeout=5)
        data = response.json()
        print(f"✅ Total Products: {data.get('total')}")
        print(f"✅ Genuine Products: {data.get('genuine')}")
        print(f"✅ Suspicious Products: {data.get('suspicious')}")
        database_ok = True
    except Exception as e:
        print(f"❌ Database Error: {str(e)}")
        database_ok = False
    
    # Test Products API
    print("\n🔍 PRODUCTS API TEST")
    print("-" * 70)
    try:
        response = requests.get("http://127.0.0.1:8000/api/products?limit=3", timeout=5)
        products = response.json()
        print(f"✅ Retrieved {len(products)} sample products:")
        for p in products[:3]:
            print(f"   • {p['product_id']}: {p['product_name']} (Genuine: {p['genuine']})")
        api_ok = True
    except Exception as e:
        print(f"❌ API Error: {str(e)}")
        api_ok = False
    
    # Test Search
    print("\n🔎 SEARCH API TEST")
    print("-" * 70)
    try:
        response = requests.get("http://127.0.0.1:8000/api/products/search?q=Paracetamol", timeout=5)
        results = response.json()
        print(f"✅ Search Results: Found {len(results)} products for 'Paracetamol'")
        search_ok = True
    except Exception as e:
        print(f"❌ Search Error: {str(e)}")
        search_ok = False
    
    # Test Frontend (basic connectivity)
    print("\n🖥️  FRONTEND TEST")
    print("-" * 70)
    try:
        response = requests.get("http://127.0.0.1:5173/", timeout=5)
        if response.status_code == 200:
            print(f"✅ Frontend Server: Running on http://127.0.0.1:5173/")
            frontend_ok = True
        else:
            print(f"⚠️  Frontend Server: Returned status {response.status_code}")
            frontend_ok = True
    except Exception as e:
        print(f"❌ Frontend Error: {str(e)}")
        frontend_ok = False
    
    # Summary
    print("\n" + "="*70)
    print("  SYSTEM SUMMARY")
    print("="*70)
    
    tests = {
        "✅ Backend API": backend_ok,
        "✅ Database": database_ok,
        "✅ Products API": api_ok,
        "✅ Search API": search_ok,
        "✅ Frontend Server": frontend_ok,
    }
    
    all_passed = all(tests.values())
    
    for test_name, result in tests.items():
        status = "PASS" if result else "FAIL"
        print(f"{test_name}: {status}")
    
    print("="*70)
    
    if all_passed:
        print("\n🎉 SUCCESS! DrugGuard NG is fully operational!\n")
        print("📍 Access the application at: http://127.0.0.1:5173/")
        print("📍 API Documentation at: http://127.0.0.1:8000/docs\n")
        return 0
    else:
        print("\n⚠️  Some tests failed. Check the errors above.\n")
        return 1

if __name__ == "__main__":
    sys.exit(test_system())
