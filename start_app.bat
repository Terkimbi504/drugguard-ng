@echo off
REM DrugGuard NG - Complete Application Startup
REM This script starts both backend and frontend in separate terminals

setlocal enabledelayedexpansion

echo.
echo ============================================================
echo   DrugGuard NG - Application Startup
echo ============================================================
echo.

REM Check if Python venv exists
if not exist ".venv" (
    echo ✗ Virtual environment not found. Run setup first.
    pause
    exit /b 1
)

REM Check if frontend dependencies exist
if not exist "frontend\node_modules" (
    echo ✗ Frontend dependencies not installed. Installing...
    cd frontend
    call npm install
    cd ..
)

echo ✓ Starting Backend (FastAPI)...
start "DrugGuard Backend" cmd /k "cd /d %cd% && .\.venv\Scripts\python.exe -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000"

timeout /t 3

echo ✓ Starting Frontend (React/Vite)...
start "DrugGuard Frontend" cmd /k "set PATH=C:\Program Files\nodejs;%PATH% && cd /d %cd%\frontend && npm run dev -- --host 127.0.0.1 --port 5173"

echo.
echo ============================================================
echo   ✅ Application Started!
echo ============================================================
echo.
echo   Backend:  http://127.0.0.1:8000
echo   Frontend: http://127.0.0.1:5173
echo.
echo   Opening application...
start http://127.0.0.1:5173/
echo.
pause
