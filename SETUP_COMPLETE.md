# DrugGuard NG - Complete Setup & Running Guide

## ✅ Final Status - FULLY OPERATIONAL

| Component | Status | URL |
|-----------|--------|-----|
| **Backend** | ✅ Running | http://127.0.0.1:8000 |
| **Frontend** | ✅ Running | http://127.0.0.1:5173 |
| **Database** | ✅ Active | SQLite with 60 demo products |
| **API** | ✅ Connected | Frontend → Backend working |

## 🚀 How to Start the Application

### Quick Start (Recommended)
Simply run the startup script:
```bash
start_app.bat
```

This will:
1. ✅ Start the backend on port 8000
2. ✅ Start the frontend on port 5173
3. ✅ Automatically open the application in your browser

### Manual Start (If Needed)

**Terminal 1 - Backend:**
```bash
cd C:\Users\user\Desktop\ode
.venv\Scripts\activate
python -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd C:\Users\user\Desktop\ode\frontend
npm run dev -- --host 127.0.0.1 --port 5173
```

## 🌐 Access Points

- **Frontend App**: http://127.0.0.1:5173/
- **API Documentation**: http://127.0.0.1:8000/docs
- **API Root**: http://127.0.0.1:8000/

## 📊 Database

- **Location**: `C:\Users\user\Desktop\ode\drugguard.db`
- **Format**: SQLite3
- **Total Products**: 60
- **Genuine Products**: 30
- **Suspicious Products**: 30

### Demo Products Include:
- Paracetamol 500mg
- Amoxicillin 500mg
- Ibuprofen 400mg
- Ciprofloxacin 500mg
- Metformin 500mg
- Amitriptyline 25mg
- Omeprazole 20mg
- Simvastatin 20mg
- Aspirin 500mg
- Vitamin C 500mg

## ✅ Verified Features

### Backend API Endpoints
- ✅ `GET /api/health` - Health check
- ✅ `GET /api/products` - List products
- ✅ `GET /api/products/search` - Search products
- ✅ `GET /api/products/stats/count` - Product statistics
- ✅ `POST /api/verify` - Verify product

### Frontend Pages
- ✅ **Home** - Landing page with overview
- ✅ **Search** - Search products by name/barcode
- ✅ **Verify** - Product verification tool
- ✅ **About** - Application information

## 🔧 Troubleshooting

### If Backend Won't Start
```bash
# Check if port 8000 is in use
Get-NetTCPConnection -LocalPort 8000 -ErrorAction SilentlyContinue

# Kill any process using port 8000
Get-Process python | Stop-Process -Force
Get-Process node | Stop-Process -Force
```

### If Frontend Won't Start
```bash
# Reinstall dependencies
cd frontend
npm install
npm run dev -- --host 127.0.0.1 --port 5173
```

### If API Connection Fails
1. Verify backend is running: http://127.0.0.1:8000/
2. Check frontend config: `frontend/src/services/api.js`
3. Should point to: `http://127.0.0.1:8000`

## 📝 Configuration Files

### Frontend API Client
- **File**: `frontend/src/services/api.js`
- **Backend URL**: `http://127.0.0.1:8000` (dev mode)
- **API Prefix**: `/api`

### Backend Configuration  
- **File**: `backend/app/config.py`
- **Database**: SQLite at root directory
- **CORS Enabled**: Yes (for localhost:5173)

### Vite Configuration
- **File**: `frontend/vite.config.js`
- **Port**: 5173
- **API Proxy**: Not used (direct connection via axios)

## 🎯 Standard Ports

- **Backend (FastAPI)**: 8000
- **Frontend (Vite)**: 5173
- **Do NOT use**: 8001, 5174, 8765 (avoid port conflicts)

## ✨ Application Ready!

The DrugGuard NG product verification system is now **fully operational** and ready to use.

**Next Steps:**
1. Run `start_app.bat` to launch both servers
2. Wait for both terminal windows to show ready status
3. Application will open automatically at http://127.0.0.1:5173/
4. Try searching for products or verifying pharmaceutical products

