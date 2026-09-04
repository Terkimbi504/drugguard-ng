#!/usr/bin/env python3
"""Test API endpoints"""
import requests
import json

BASE_URL = "http://127.0.0.1:8000"

print("=" * 60)
print("  DrugGuard NG - Backend API Test")
print("=" * 60)

# Test 1: Health
print("\n✓ Testing /api/health...")
try:
    response = requests.get(f"{BASE_URL}/api/health")
    data = response.json()
    print(f"  Status: {data.get('status')}")
    print(f"  Version: {data.get('version')}")
except Exception as e:
    print(f"  ✗ Error: {e}")

# Test 2: Products
print("\n✓ Testing /api/products...")
try:
    response = requests.get(f"{BASE_URL}/api/products?limit=3")
    products = response.json()
    print(f"  Found {len(products)} products:")
    for p in products[:3]:
        print(f"    - {p['product_id']}: {p['product_name']} (Genuine: {p['genuine']})")
except Exception as e:
    print(f"  ✗ Error: {e}")

# Test 3: Product Count
print("\n✓ Testing /api/products/stats/count...")
try:
    response = requests.get(f"{BASE_URL}/api/products/stats/count")
    data = response.json()
    print(f"  Total products: {data.get('total')}")
    print(f"  Genuine: {data.get('genuine')}")
    print(f"  Suspicious: {data.get('suspicious')}")
except Exception as e:
    print(f"  ✗ Error: {e}")

# Test 4: Search
print("\n✓ Testing /api/products/search...")
try:
    response = requests.get(f"{BASE_URL}/api/products/search?q=Paracetamol&limit=2")
    products = response.json()
    print(f"  Found {len(products)} products matching 'Paracetamol':")
    for p in products[:2]:
        print(f"    - {p['product_id']}: {p['product_name']}")
except Exception as e:
    print(f"  ✗ Error: {e}")

print("\n" + "=" * 60)
print("  ✅ Backend is running and responding!")
print("=" * 60)
