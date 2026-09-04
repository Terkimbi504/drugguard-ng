#!/usr/bin/env python3
"""Load demo product data into the database"""
import sys
sys.path.insert(0, 'backend')

from app.database import SessionLocal
from app.models import Product
import pandas as pd

# Check current count
db = SessionLocal()
current_count = db.query(Product).count()
print(f"Products currently in DB: {current_count}")

# Load CSV
df = pd.read_csv('backend/data/products.csv')

# Add missing products
added = 0
for _, row in df.iterrows():
    existing = db.query(Product).filter_by(product_id=str(row['product_id'])).first()
    if not existing:
        # Convert price safely
        try:
            price = float(row.get('price', 0)) if row.get('price') else None
        except (ValueError, TypeError):
            price = None
        
        product = Product(
            product_id=str(row['product_id']),
            product_name=row['product_name'],
            generic_name=row.get('generic_name'),
            strength=row.get('strength'),
            dosage_form=row.get('dosage_form'),
            manufacturer=row.get('manufacturer'),
            nafdac_number=row.get('nafdac_number'),
            barcode=row.get('barcode'),
            batch_number=row.get('batch_number'),
            expiry_date=row.get('expiry_date'),
            distributor=row.get('distributor'),
            packaging_version=row.get('packaging_version'),
            price=price,
            nafdac_registered=str(row.get('nafdac_registered', False)).lower() == 'true',
            manufacturer_verified=str(row.get('manufacturer_verified', False)).lower() == 'true',
            registration_valid=str(row.get('registration_valid', False)).lower() == 'true',
            barcode_verified=str(row.get('barcode_verified', False)).lower() == 'true',
            batch_verified=str(row.get('batch_verified', False)).lower() == 'true',
            expiry_valid=str(row.get('expiry_valid', False)).lower() == 'true',
            packaging_match=str(row.get('packaging_match', False)).lower() == 'true',
            distributor_verified=str(row.get('distributor_verified', False)).lower() == 'true',
            price_anomaly=str(row.get('price_anomaly', False)).lower() == 'true',
            genuine=str(row.get('genuine', False)).lower() == 'true',
        )
        db.add(product)
        added += 1

db.commit()

# Verify
final_count = db.query(Product).count()
print(f"✓ Products added: {added}")
print(f"✓ Total products in DB: {final_count}")

# Show sample
products = db.query(Product).limit(3).all()
for p in products:
    print(f"  - {p.product_id}: {p.product_name} (Genuine: {p.genuine})")

db.close()
