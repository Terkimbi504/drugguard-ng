#!/usr/bin/env python3
"""
Generate demo dataset for DrugGuard NG
This script creates a CSV file with 100+ synthetic drug product records
Run this script to generate backend/data/products.csv
"""

import csv
import os
from datetime import datetime, timedelta
import random

# Create data directory if it doesn't exist
os.makedirs('backend/data', exist_ok=True)

# Seed random for reproducibility
random.seed(42)

products_data = []

# Known verified products
verified_products = [
    {"name": "Paracetamol", "strength": "500mg", "form": "Tablet", "generic": "Paracetamol"},
    {"name": "Amoxicillin", "strength": "500mg", "form": "Capsule", "generic": "Amoxicillin"},
    {"name": "Ibuprofen", "strength": "400mg", "form": "Tablet", "generic": "Ibuprofen"},
    {"name": "Metformin", "strength": "500mg", "form": "Tablet", "generic": "Metformin"},
    {"name": "Lisinopril", "strength": "10mg", "form": "Tablet", "generic": "Lisinopril"},
    {"name": "Aspirin", "strength": "100mg", "form": "Tablet", "generic": "Acetylsalicylic Acid"},
    {"name": "Omeprazole", "strength": "20mg", "form": "Capsule", "generic": "Omeprazole"},
    {"name": "Atorvastatin", "strength": "20mg", "form": "Tablet", "generic": "Atorvastatin"},
    {"name": "Doxycycline", "strength": "100mg", "form": "Capsule", "generic": "Doxycycline"},
    {"name": "Cephalexin", "strength": "500mg", "form": "Capsule", "generic": "Cephalexin"},
]

manufacturers = [
    "GlaxoSmithKline", "Pfizer", "Novartis", "Johnson & Johnson",
    "Merck", "Bristol-Myers Squibb", "AbbVie", "Roche",
    "Eli Lilly", "Sanofi", "Bayer", "AstraZeneca",
    "Amgen", "Gilead Sciences", "Regeneron", "Moderna"
]

distributors = [
    "HealthCare Plus", "MediSupply Ltd", "PharmaCare Distribution",
    "Medical Solutions", "DrugGuard Distributors", "Prime Pharma",
    "Global Health Supply", "National Pharma"
]

# Generate genuine products
product_id_counter = 1000

print("Generating genuine products...")
for i, product in enumerate(verified_products):
    for variant in range(4):  # 4 variants per product
        base_price = random.uniform(500, 5000)
        price = base_price + (variant * random.uniform(100, 500))
        
        expiry = datetime.now() + timedelta(days=random.randint(180, 900))
        
        is_genuine = random.random() > 0.3  # 70% genuine
        
        products_data.append({
            "product_id": f"DG{product_id_counter}",
            "product_name": f"{product['name']} {product['strength']}",
            "generic_name": product['generic'],
            "strength": product['strength'],
            "dosage_form": product['form'],
            "manufacturer": random.choice(manufacturers),
            "nafdac_number": f"NAFD/{'A' if is_genuine else 'X'}/{product_id_counter:05d}",
            "barcode": f"900{product_id_counter % 10000:04d}",
            "batch_number": f"BATCH-{product_id_counter}-{random.randint(100, 999)}",
            "expiry_date": expiry.strftime("%Y-%m-%d"),
            "distributor": random.choice(distributors),
            "packaging_version": f"v{random.randint(1, 3)}",
            "price": round(price, 2),
            "nafdac_registered": is_genuine,
            "manufacturer_verified": is_genuine and random.random() > 0.1,
            "registration_valid": is_genuine and random.random() > 0.05,
            "barcode_verified": is_genuine and random.random() > 0.15,
            "batch_verified": is_genuine and random.random() > 0.1,
            "expiry_valid": random.random() > 0.1,
            "packaging_match": is_genuine and random.random() > 0.15,
            "distributor_verified": is_genuine and random.random() > 0.2,
            "price_anomaly": not is_genuine or random.random() > 0.8,
            "genuine": is_genuine,
        })
        product_id_counter += 1

# Add suspicious/incomplete products
print("Generating suspicious products...")
suspicious_products = [
    "Unknown Medicine Pro", "CounterFlex Drug", "Suspicion Labs",
    "Unregistered Pharma", "Grey Market Med", "Replica Cure",
    "UnVerified Supply", "Black Market Pharma", "Questionable Labs",
    "Dodgy Pharmacy"
]

for i, product_name in enumerate(suspicious_products):
    for variant in range(2):
        products_data.append({
            "product_id": f"DG{product_id_counter}",
            "product_name": f"{product_name} {random.choice(['500mg', '250mg', '100mg'])}",
            "generic_name": "Unknown",
            "strength": random.choice(['500mg', '250mg', '100mg']),
            "dosage_form": random.choice(['Tablet', 'Capsule', 'Syrup']),
            "manufacturer": "Unknown Manufacturer",
            "nafdac_number": f"NAFD/INVALID/{random.randint(10000, 99999)}",
            "barcode": f"999{random.randint(1000, 9999)}",
            "batch_number": f"SUSPICIOUS-{random.randint(100000, 999999)}",
            "expiry_date": (datetime.now() - timedelta(days=random.randint(1, 730))).strftime("%Y-%m-%d"),
            "distributor": "Unknown",
            "packaging_version": "",
            "price": round(random.uniform(200, 1000), 2),
            "nafdac_registered": False,
            "manufacturer_verified": False,
            "registration_valid": False,
            "barcode_verified": False,
            "batch_verified": False,
            "expiry_valid": False,
            "packaging_match": False,
            "distributor_verified": False,
            "price_anomaly": True,
            "genuine": False,
        })
        product_id_counter += 1

# Add products with partial information
print("Generating products with partial information...")
for i in range(20):
    products_data.append({
        "product_id": f"DG{product_id_counter}",
        "product_name": f"Partial Info Drug {i}",
        "generic_name": random.choice([None, "Generic Name"]) or "",
        "strength": random.choice([None, "500mg", "250mg"]) or "",
        "dosage_form": random.choice(['Tablet', 'Capsule', None]) or "",
        "manufacturer": random.choice([None, random.choice(manufacturers)]) or "",
        "nafdac_number": "" if random.random() > 0.5 else f"NAFD/X/{random.randint(10000, 99999)}",
        "barcode": "" if random.random() > 0.6 else f"900{random.randint(1000, 9999)}",
        "batch_number": "",
        "expiry_date": "" if random.random() > 0.7 else (datetime.now() + timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d"),
        "distributor": "" if random.random() > 0.5 else random.choice(distributors),
        "packaging_version": "",
        "price": "" if random.random() > 0.6 else round(random.uniform(300, 3000), 2),
        "nafdac_registered": False,
        "manufacturer_verified": random.random() > 0.7,
        "registration_valid": False,
        "barcode_verified": random.random() > 0.8,
        "batch_verified": False,
        "expiry_valid": random.random() > 0.5,
        "packaging_match": False,
        "distributor_verified": random.random() > 0.7,
        "price_anomaly": random.random() > 0.6,
        "genuine": False,
    })
    product_id_counter += 1

# Write to CSV
csv_path = "backend/data/products.csv"
print(f"\nWriting {len(products_data)} records to {csv_path}...")

fieldnames = [
    "product_id", "product_name", "generic_name", "strength", "dosage_form",
    "manufacturer", "nafdac_number", "barcode", "batch_number", "expiry_date",
    "distributor", "packaging_version", "price", "nafdac_registered",
    "manufacturer_verified", "registration_valid", "barcode_verified",
    "batch_verified", "expiry_valid", "packaging_match", "distributor_verified",
    "price_anomaly", "genuine"
]

with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(products_data)

print(f"✅ Dataset created successfully!")
print(f"   Location: {csv_path}")
print(f"   Total records: {len(products_data)}")
print(f"   Genuine products: {sum(1 for p in products_data if p['genuine'])}")
print(f"   Suspicious products: {sum(1 for p in products_data if not p['genuine'])}")
