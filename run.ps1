# Mental Model Hub - Backend Startup Script for PowerShell

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Mental Model Hub - Backend Startup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

Write-Host ""
Write-Host "Starting Flask backend..." -ForegroundColor Green
Write-Host "Access frontend at: file://$(Get-Location)/index.html" -ForegroundColor Green
Write-Host "Backend API: http://localhost:5000" -ForegroundColor Green
Write-Host ""
Write-Host "Press CTRL+C to stop the server" -ForegroundColor Yellow
Write-Host ""

python app.py

Read-Host "Press Enter to exit"
