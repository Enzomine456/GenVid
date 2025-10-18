@echo off
echo GenVid - Fly.io Deployment Helper for Windows
echo ==============================================
echo.

echo 1. Checking if flyctl is installed...
echo ----------------------------------------
flyctl version >nul 2>&1
if %errorlevel% == 0 (
    echo ✓ flyctl is installed
    flyctl version
) else (
    echo ✗ flyctl is not installed or not in PATH
    echo.
    echo Please install flyctl using:
    echo winget install flyctl
    echo.
    echo Then close and reopen this command prompt
    echo.
    pause
    exit /b
)

echo.
echo 2. Running fix script...
echo ------------------------
python fly_launch_fix.py

echo.
echo 3. Deploying to Fly.io...
echo ------------------------
echo If this is your first time deploying, you may need to login:
echo flyctl auth login
echo.
echo To deploy, run:
echo flyctl deploy
echo.
echo For a fresh launch (if needed), run:
echo flyctl launch --force
echo.

pause