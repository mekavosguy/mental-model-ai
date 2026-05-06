@echo off
echo ========================================
echo Mental Model Hub - Backend Startup
echo ========================================
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Starting Flask backend on http://localhost:5000
echo.
echo Press CTRL+C to stop the server
echo.
python app.py
pause
