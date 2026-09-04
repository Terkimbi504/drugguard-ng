"""Manually load demo data into database"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from app.database import SessionLocal, Base, engine
from app.models import Product
import pandas as pd

# Create all tables
Base.metadata.create_all(bind=engine)

# Read CSV
csv_path = os.path.join(os.path.dirname(__file__), 'backend', 'data', 'products.csv')
print(f"Loading data from: {csv_path}")

if not os.path.exists(csv_path):
    print(f"ERROR: CSV file not found at {csv_path}")
    sys.exit(1)

df = pd.read_csv(csv_path)
print(f"Read {len(df)} products from CSV")

# Create session
db = SessionLocal()

# Load data
count = 0
for _, row in df.iterrows():
    try:
        # Handle price conversion safely
        price_val = row.get('price')
        if price_val and price_val not in ['False', False, 'None', None]:
            try:
                price = float(price_val)
            except (ValueError, TypeError):
                price = None
        else:
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
            nafdac_registered=bool(row.get('nafdac_registered', False)),
            manufacturer_verified=bool(row.get('manufacturer_verified', False)),
            registration_valid=bool(row.get('registration_valid', False)),
            barcode_verified=bool(row.get('barcode_verified', False)),
            batch_verified=bool(row.get('batch_verified', False)),
            expiry_valid=bool(row.get('expiry_valid', False)),
            packaging_match=bool(row.get('packaging_match', False)),
            distributor_verified=bool(row.get('distributor_verified', False)),
            price_anomaly=bool(row.get('price_anomaly', False)),
            genuine=bool(row.get('genuine', False)),
        )
        db.add(product)
        count += 1
    except Exception as e:
        print(f"Error loading row {count}: {str(e)}")
        print(f"Row data: {row}")
        continue

db.commit()
db.close()

print(f"✓ Successfully loaded {count} products into database!")

# Verify
db = SessionLocal()
total = db.query(Product).count()
print(f"Database now contains {total} products")
db.close()
