"""Check database contents"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from app.database import SessionLocal
from app.models import Product

# Create session
db = SessionLocal()

# Count products
count = db.query(Product).count()
print(f"Total products in database: {count}")

# List first 5 products
if count > 0:
    products = db.query(Product).limit(5).all()
    for product in products:
        print(f"- {product.product_name} (ID: {product.id}, Barcode: {product.barcode})")
else:
    print("No products found in database!")

db.close()
