# DrugGuard NG

**AI-assisted Drug Product Verification & Suspicion Classifier**

An educational and demonstration prototype for identifying potentially suspicious drug product entries using machine learning and rule-based verification.

---

## ⚠️ IMPORTANT DISCLAIMER

**This is an AI-assisted screening prototype for educational and demonstration purposes only.**

- **Does NOT replace official NAFDAC verification** or laboratory testing
- **Does NOT replace professional medical advice** or qualified healthcare practitioners
- Uses **synthetic demonstration data only** - not connected to any real regulatory system
- Results are **educational predictions only** and should never be the sole basis for medicine verification decisions

Always consult qualified pharmacists, healthcare professionals, and official regulatory bodies for authentic medicine verification.

---

## Features

✅ **Product Search & Database Lookup**
- Search by product name, NAFDAC number, barcode, or batch number
- View detailed product information
- Real-time database queries

✅ **Verification System**
- 9 verification indicators checked per product
- Risk scoring from 0-100
- Clear classification: Genuine / Suspicious / Review Required / Not Found

✅ **Machine Learning Classification**
- Trained on synthetic demo dataset (100+ records)
- Supervised classification models (Random Forest, Logistic Regression)
- Performance metrics: Accuracy, Precision, Recall, F1 Score

✅ **Transparent Explanations**
- AI-powered explanation engine
- Clear reasoning for classifications
- Distinction between ML prediction and risk assessment

✅ **Professional Dashboard**
- Demo database statistics
- Model performance metrics
- Responsive design for mobile and desktop

✅ **Automated Testing**
- Comprehensive backend tests
- API endpoint validation
- Model evaluation tests

---

## Technology Stack

### Backend
- **Python 3.11+**
- **FastAPI** - Modern web framework
- **Scikit-learn** - Machine learning
- **Pandas & NumPy** - Data processing
- **SQLAlchemy** - ORM
- **SQLite** - Database
- **Uvicorn** - ASGI server

### Frontend
- **React 18** - UI framework
- **Vite** - Build tool
- **Tailwind CSS** - Styling
- **Axios** - HTTP client
- **React Router** - Navigation
- **React Icons** - Icon library

---

## Architecture

```
DrugGuard NG/
├── backend/
│   ├── app/
│   │   ├── main.py (FastAPI application)
│   │   ├── config.py (Configuration)
│   │   ├── database.py (Database setup)
│   │   ├── models/ (SQLAlchemy models)
│   │   ├── schemas/ (Pydantic schemas)
│   │   ├── routes/ (API endpoints)
│   │   ├── services/ (Business logic)
│   │   └── ml/ (Machine learning)
│   ├── data/
│   │   └── products.csv (Demo dataset)
│   ├── tests/ (Automated tests)
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/ (Reusable components)
│   │   ├── pages/ (Page components)
│   │   ├── services/ (API client)
│   │   ├── App.jsx (Main app)
│   │   └── main.jsx (Entry point)
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js
│
├── scripts/
│   ├── setup_windows.bat (Automated setup)
│   └── run_project.bat (Start services)
│
└── README.md
```

---

## Machine Learning Approach

### Dataset
- **100+ synthetic records** - fictional demo drug products
- **Balanced classes** - mix of genuine and suspicious products
- **9 verification features** - registration, barcode, batch, expiry, etc.
- **Target variable** - genuine (1) or suspicious (0)

### Model Selection
- Trained **2 candidate models** for comparison:
  1. **Logistic Regression**
  2. **Random Forest** (Default - better recall for suspicious detection)

### Evaluation Metrics
- **Accuracy**: Overall correctness
- **Precision**: Accuracy of positive predictions
- **Recall**: Ability to detect suspicious products (prioritized)
- **F1 Score**: Harmonic mean of precision and recall
- **Confusion Matrix**: Detailed classification performance

### Important - No Data Leakage
- ✅ Training/test split with stratification
- ✅ The target label "genuine" is NOT used as a feature
- ✅ Only legitimate verification indicators are used
- ✅ Proper cross-validation approach

---

## Risk Scoring System

Products are scored 0-100 based on weighted verification indicators:

| Indicator | Weight | Points |
|-----------|--------|--------|
| Registration Missing | 30 | +30 |
| Manufacturer Unverified | 20 | +20 |
| Registration Invalid | 20 | +20 |
| Barcode Mismatch | 10 | +10 |
| Batch Mismatch | 10 | +10 |
| Expiry Invalid | 5 | +5 |
| Packaging Mismatch | 15 | +15 |
| Distributor Unverified | 15 | +15 |
| Price Anomaly | 10 | +10 |

**Risk Levels:**
- 0-20: LOW RISK (Likely Genuine)
- 21-50: MODERATE RISK (Requires Review)
- 51-100: HIGH RISK (Suspicious)

---

## API Endpoints

### Health
```
GET /api/health
```

### Products
```
GET /api/products                          # List products
GET /api/products/search?q=                # Search products
GET /api/products/barcode/{barcode}        # Get by barcode
GET /api/products/{id}                     # Get by ID
GET /api/products/stats/count              # Get statistics
```

### Verification
```
POST /api/verify                           # Verify a product
```

### Evaluation
```
GET /api/evaluation                        # Get ML metrics
```

### Documentation
```
GET /docs                                  # Interactive API docs (Swagger)
```

---

## Installation & Setup

### Prerequisites
- Python 3.11+
- Node.js 18+
- Git

### Quick Setup (Windows)

1. **Clone or extract the project**
```bash
cd c:\Users\user\Desktop\ode
```

2. **Run automated setup**
```bash
scripts\setup_windows.bat
```

This will:
- ✅ Check Python and Node.js
- ✅ Create Python virtual environment
- ✅ Install backend dependencies
- ✅ Generate demo dataset
- ✅ Train ML model
- ✅ Install frontend dependencies
- ✅ Run tests

3. **Start the application**
```bash
scripts\run_project.bat
```

This opens two terminal windows:
- **Backend**: http://drugguard-ng.vercel.app
- **Frontend**: http://drugguard-ng vercel.app1

---

## Manual Setup (If Preferred)

### Backend Setup
```bash
# Activate virtual environment
.venv\Scripts\activate.bat

# Install dependencies
pip install -r backend\requirements.txt

# Generate demo data
cd backend
python seed_data.py

# Train ML model
python app\ml\train_model.py

# Start backend
uvicorn app.main:app --reload
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

---

## Usage

### 1. Verify a Product
- Navigate to "Verify Product"
- Enter product information (name, barcode, batch, etc.)
- Click "Verify Product"
- View risk score, classification, and explanation

### 2. Search Database
- Navigate to "Search"
- Search by product name, NAFDAC number, barcode, or batch
- View product details and verification status

### 3. View Dashboard
- Home page shows demo database statistics
- See genuine vs suspicious product counts
- View model performance metrics

### 4. Review API Documentation
- Visit http://localhost:8000/docs
- Interactive Swagger UI for all endpoints
- Try API calls directly

---

## Testing

### Run Backend Tests
```bash
cd backend
python -m pytest tests/ -v
```

### Test Coverage
- ✅ Health endpoint
- ✅ Product search
- ✅ Barcode lookup
- ✅ Verification endpoint
- ✅ Risk calculation
- ✅ ML predictions
- ✅ Invalid input handling

---

## Database

### SQLite (Default)
- Automatically initialized on first run
- Stored as `drugguard.db`
- Contains demo product data

### Demo Data
- 100+ synthetic records
- Mix of verified and suspicious products
- Realistic product information
- Verification indicators for each product

---

## Deployment

### Frontend Deployment (Vercel/Netlify)
```bash
cd frontend
npm run build
```
Deploy the `dist/` folder to Vercel or Netlify

### Backend Deployment (Render/Railway)
```bash
# Create Procfile
web: uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT
```
Push to GitHub and deploy to Render or Railway

### Environment Variables
```
FRONTEND_URL=https://your-frontend-domain.com
BACKEND_URL=https://your-backend-domain.com
ENVIRONMENT=production
DEBUG=false

## Project Structure Details

### Backend Services
- **Verification Service**: Product search and indicator checking
- **Risk Service**: Risk score calculation
- **Explanation Service**: Human-readable explanations
- **ML Service**: Machine learning predictions

### Frontend Components
- **Header**: Navigation and branding
- **VerificationForm**: Product input form
- **ResultDisplay**: Verification results
- **Footer**: Footer with important notices

### Pages
- **Home**: Dashboard and statistics
- **Verify**: Verification workflow
- **Search**: Product database search
- **About**: System information and disclaimers

---

## Future Improvements

- [ ] Live NAFDAC API integration
- [ ] Barcode scanner support (camera/QR code)
- [ ] User authentication
- [ ] Result history tracking
- [ ] Admin dashboard
- [ ] Advanced analytics
- [ ] Multi-language support
- [ ] Mobile app version

---

## Important Notes

### Demo Data
- All products and NAFDAC numbers in the database are fictional/synthetic
- No real medicines or registration numbers
- For educational demonstration only

### ML Metrics
- Performance metrics are based on synthetic data
- Should not be interpreted as real-world performance
- Demonstration of ML pipeline and model selection

### Use Cases
- ✅ Educational demonstration
- ✅ AI/ML portfolio project
- ✅ Full-stack web development showcase
- ✅ Healthcare tech concepts
- ❌ Production drug verification
- ❌ Official regulatory compliance
## License & Attribution

This is an educational prototype developed as a demonstration project. It uses fictional data and is not affiliated with any official regulatory body.

---

## Contact & Support

For questions about this educational project, refer to the documentation and code comments throughout the repository.

---

**Last Updated**: December 2024
**Status**: Complete & Tested
**Version**: 1.0.0
