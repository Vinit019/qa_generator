@echo off
echo ========================================
echo Question Answer Generator - Environment Setup
echo ========================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% == 0 (
    set PYTHON_CMD=python
    goto :create_env
)

py --version >nul 2>&1
if %errorlevel% == 0 (
    set PYTHON_CMD=py
    goto :create_env
)

echo Python is not installed or not in PATH!
echo.
echo Please install Python first:
echo 1. Go to https://www.python.org/downloads/
echo 2. Download and install Python 3.7 or higher
echo 3. Make sure to check "Add Python to PATH" during installation
echo 4. Restart your computer after installation
echo 5. Run this script again
echo.
pause
exit /b 1

:create_env
echo Python found: %PYTHON_CMD%
%PYTHON_CMD% --version
echo.

REM Create virtual environment
echo Creating virtual environment...
%PYTHON_CMD% -m venv question_generator_env
if %errorlevel% neq 0 (
    echo Error creating virtual environment!
    pause
    exit /b 1
)

echo Virtual environment created successfully!
echo.

REM Activate virtual environment
echo Activating virtual environment...
call question_generator_env\Scripts\activate.bat

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo Installing required packages...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error installing packages!
    echo Please check your internet connection and try again.
    pause
    exit /b 1
)

REM Download NLTK data
echo Downloading NLTK data...
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('averaged_perceptron_tagger')"

REM Create necessary directories
echo Creating directories...
if not exist "uploads" mkdir uploads
if not exist "outputs" mkdir outputs
if not exist "templates" mkdir templates
if not exist "static" mkdir static

echo.
echo ========================================
echo Environment Setup Complete!
echo ========================================
echo.
echo Your virtual environment is ready!
echo.
echo To run the project:
echo 1. Double-click "run_project.bat"
echo 2. Or run these commands in Command Prompt:
echo    call question_generator_env\Scripts\activate.bat
echo    python app.py
echo.
echo Then open your browser and go to: http://localhost:5000
echo.
pause
