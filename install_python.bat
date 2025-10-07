@echo off
echo ========================================
echo Question Answer Generator - Python Setup
echo ========================================
echo.
echo This script will help you install Python and set up the project.
echo.

REM Check if Python is already installed
python --version >nul 2>&1
if %errorlevel% == 0 (
    echo Python is already installed!
    python --version
    goto :setup_project
)

py --version >nul 2>&1
if %errorlevel% == 0 (
    echo Python is already installed!
    py --version
    goto :setup_project
)

echo Python is not installed on your system.
echo.
echo Please follow these steps to install Python:
echo.
echo 1. Go to https://www.python.org/downloads/
echo 2. Download the latest Python version (3.7 or higher)
echo 3. Run the installer
echo 4. IMPORTANT: Check "Add Python to PATH" during installation
echo 5. Complete the installation
echo.
echo After installing Python, run this script again.
echo.
pause
exit /b 1

:setup_project
echo.
echo Setting up the project environment...
echo.

REM Create virtual environment
echo Creating virtual environment...
python -m venv question_generator_env
if %errorlevel% neq 0 (
    py -m venv question_generator_env
    if %errorlevel% neq 0 (
        echo Error creating virtual environment!
        pause
        exit /b 1
    )
)

echo Virtual environment created successfully!
echo.

REM Activate virtual environment
echo Activating virtual environment...
call question_generator_env\Scripts\activate.bat

echo Installing required packages...
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To run the project:
echo 1. Double-click "run_project.bat"
echo 2. Or open Command Prompt and run:
echo    call question_generator_env\Scripts\activate.bat
echo    python app.py
echo.
echo Then open your browser and go to: http://localhost:5000
echo.
pause
