"""Load demo products data directly"""
import sys
sys.path.insert(0, 'backend')

from app.database import SessionLocal, Base, engine
from app.models import Product
import pandas as pd
import os

# Remove old database if it exists
if os.path.exists('drugguard.db'):
    os.remove('drugguard.db')

# Create all tables
Base.metadata.create_all(bind=engine)

# Read CSV
df = pd.read_csv('backend/data/products.csv')

# Create session
db = SessionLocal()

# Load data
for _, row in df.iterrows():
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
        price=float(row.get('price', 0)) if row.get('price') else None,
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

# Commit
db.commit()

# Verify
count = db.query(Product).count()
print(f"✓ Database initialized with {count} products")

# Show sample
products = db.query(Product).limit(3).all()
for p in products:
    print(f"  - {p.product_id}: {p.product_name} (Genuine: {p.genuine})")

db.close()
