# DrugGuard NG - Quick Start Guide

## 🚀 For Beginners: Complete Step-by-Step Setup

### Prerequisites
- **Python 3.11+** - [Download here](https://www.python.org/downloads/)
- **Node.js 18+** - [Download here](https://nodejs.org/)
- **Windows** (this guide)

---

## Option 1: Automated Setup (Recommended)

### Step 1: Run Setup Script
```bash
cd c:\Users\user\Desktop\ode
scripts\setup_windows.bat
```

This will automatically:
- ✅ Check Python and Node.js
- ✅ Create virtual environment
- ✅ Install all dependencies
- ✅ Generate demo data
- ✅ Train ML model
- ✅ Install frontend packages
- ✅ Run tests

### Step 2: Start Services
```bash
scripts\run_project.bat
```

This opens two windows with:
- **Backend**: http://localhost:8000
- **Frontend**: http://localhost:5173

### Step 3: Open in Browser
- Visit: http://localhost:5173
- Verify Product at: http://localhost:5173/verify
- API Docs at: http://localhost:8000/docs

---

## Option 2: Manual Setup (If Automated Fails)

### Step 1: Create Virtual Environment
```bash
cd c:\Users\user\Desktop\ode
python -m venv .venv
.venv\Scripts\activate.bat
```

### Step 2: Install Backend Dependencies
```bash
pip install -r backend\requirements.txt
```

### Step 3: Prepare Data
The demo dataset is already created in `backend\data\products.csv`

### Step 4: Train ML Model
```bash
cd backend
python app\ml\train_model.py
cd ..
```

If this fails, the application will use rule-based predictions instead.

### Step 5: Start Backend
```bash
uvicorn backend.app.main:app --reload
```

Backend is now running at: http://localhost:8000

### Step 6: Start Frontend (in new terminal)
```bash
cd frontend
npm install
npm run dev
```

Frontend is now running at: http://localhost:5173

---

## 🧪 Testing the Application

### Test 1: Health Check
Visit: http://localhost:8000/api/health

Should show:
```json
{
  "status": "ok",
  "version": "1.0.0",
  "environment": "demo"
}
```

### Test 2: Verify a Product
1. Go to http://localhost:5173/verify
2. Enter product name: "Paracetamol 500mg"
3. Click "Verify Product"
4. Should see: GENUINE (Low Risk)

### Test 3: Search Products
1. Go to http://localhost:5173/search
2. Search for: "Paracetamol"
3. Should find multiple results

### Test 4: API Documentation
Visit: http://localhost:8000/docs

Interactive API documentation where you can test endpoints.

---

## 🐛 Troubleshooting

### Python Not Found
```
Error: "Python was not found"
```
Solution: Python not installed or not in PATH
- Download from https://www.python.org
- During installation, check "Add Python to PATH"
- Restart terminal/command prompt

### Port Already in Use
```
Error: Address already in use
```
Solution: Port 8000 or 5173 is already taken
```bash
# Find and kill process
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Or use different ports
uvicorn backend.app.main:app --port 9000
cd frontend && npm run dev -- --port 5174
```

### Module Not Found Errors
```
Error: ModuleNotFoundError: No module named 'fastapi'
```
Solution: Dependencies not installed
```bash
pip install -r backend\requirements.txt
```

### Frontend Stuck on Loading
- Make sure backend is running (http://localhost:8000)
- Check browser console for errors (F12)
- Try refreshing page (Ctrl+R)

### Model Training Fails
The application will still work with rule-based predictions if training fails.

---

## 📚 What Each Component Does

### Backend (FastAPI)
- REST API for product verification
- Database with demo products
- ML model predictions
- Risk scoring
- Explanation generation

**Files:**
- `backend/app/main.py` - Main application
- `backend/app/routes/` - API endpoints
- `backend/app/services/` - Business logic
- `backend/data/products.csv` - Demo dataset

### Frontend (React + Vite)
- Beautiful user interface
- Product verification form
- Search functionality
- Result display
- Dashboard

**Files:**
- `frontend/src/App.jsx` - Main component
- `frontend/src/pages/` - Page components
- `frontend/src/components/` - UI components
- `frontend/src/services/api.js` - API client

### Database (SQLite)
- Stores demo products
- Auto-created on first run
- File: `backend/app/drugguard.db`

---

## 🎯 Key Features to Test

### 1. Genuine Product
Enter: "Paracetamol 500mg"
Expected: GENUINE (Low Risk 0-20)

### 2. Suspicious Product
Enter: "Unknown Medicine Pro"
Expected: SUSPICIOUS (High Risk 51-100)

### 3. Unknown Product
Enter: "XYZ Drug 123mg"
Expected: NOT FOUND (Unable to Verify)

### 4. Search Products
Products are searchable by:
- Product Name
- NAFDAC Number
- Barcode
- Batch Number

---

## 🔐 Important Disclaimer

⚠️ **This is a DEMO/EDUCATIONAL system**

- ❌ Does NOT connect to real NAFDAC database
- ❌ Does NOT replace official verification
- ❌ Uses fictional/synthetic data only
- ❌ Should NOT be used for real medicine verification

**Always consult:**
- Licensed pharmacists
- Healthcare professionals  
- Official regulatory bodies
- Laboratory testing

---

## 📖 API Endpoints

### Health
- `GET /api/health` - Check API status

### Products
- `GET /api/products` - List all products
- `GET /api/products/search?q=` - Search products
- `GET /api/products/barcode/{barcode}` - Get by barcode
- `GET /api/products/{id}` - Get by ID
- `GET /api/products/stats/count` - Get statistics

### Verification  
- `POST /api/verify` - Verify a product

### Evaluation
- `GET /api/evaluation` - ML model metrics

---

## 🛠️ Development Tips

### Enable Auto-Reload
Backend already has `--reload` flag, so changes auto-load

### Debug Mode
Frontend has React DevTools (install browser extension)

### View Database
Download SQLite Browser: https://sqlitebrowser.org/

Then open: `backend/app/drugguard.db`

### Modify Risk Weights
Edit: `backend/app/config.py`
Change `RISK_WEIGHTS` dictionary to adjust scoring

---

## 🚀 Next Steps

1. **Explore the Code**
   - Read `backend/app/main.py` to understand FastAPI setup
   - Read `frontend/src/App.jsx` to understand React structure
   - Review `backend/app/services/` for business logic

2. **Modify Demo Data**
   - Edit `backend/data/products.csv` to add/remove products
   - Restart backend to reload

3. **Deploy**
   - See README.md for deployment instructions
   - Frontend → Vercel/Netlify
   - Backend → Render/Railway

4. **Add Features**
   - Barcode scanner support
   - User authentication
   - Result history
   - Export reports

---

## 📞 Need Help?

Check these files:
- `README.md` - Comprehensive documentation
- `backend/` - Backend code and comments
- `frontend/` - Frontend code and comments
- `scripts/` - Setup and run scripts

---

**You're all set! Start testing DrugGuard NG now!** 🎉
