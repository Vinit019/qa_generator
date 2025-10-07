@echo off
echo ========================================
echo Question Answer Generator
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "question_generator_env" (
    echo Virtual environment not found!
    echo Please run "install_python.bat" first to set up the environment.
    echo.
    pause
    exit /b 1
)

REM Activate virtual environment
echo Activating virtual environment...
call question_generator_env\Scripts\activate.bat

REM Check if packages are installed
echo Checking if required packages are installed...
python -c "import flask" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing required packages...
    pip install -r requirements.txt
    echo.
    echo Downloading NLTK data...
    python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('averaged_perceptron_tagger')"
)

echo.
echo Starting the Question Answer Generator...
echo.
echo The application will start at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.

REM Start the Flask application
python app.py

echo.
echo Application stopped.
pause
