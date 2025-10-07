@echo off
echo ========================================
echo Push to GitHub Repository
echo ========================================
echo.

REM Check if Git is installed
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Git is not installed!
    echo.
    echo Please install Git first:
    echo 1. Go to https://git-scm.com/download/win
    echo 2. Download and install Git
    echo 3. Restart Command Prompt
    echo 4. Run this script again
    echo.
    pause
    exit /b 1
)

echo Git is installed!
git --version
echo.

REM Initialize Git repository
echo Initializing Git repository...
git init
if %errorlevel% neq 0 (
    echo Error initializing Git repository!
    pause
    exit /b 1
)

REM Add all files
echo Adding all files...
git add .
if %errorlevel% neq 0 (
    echo Error adding files!
    pause
    exit /b 1
)

REM Commit files
echo Committing files...
git commit -m "Initial commit: Question Answer Generator - Complete project with Flask web app, document processing, question generation, and export functionality"
if %errorlevel% neq 0 (
    echo Error committing files!
    pause
    exit /b 1
)

REM Add remote repository
echo Adding remote repository...
git remote add origin https://github.com/Vinit019/qa_generator.git
if %errorlevel% neq 0 (
    echo Remote already exists, updating...
    git remote set-url origin https://github.com/Vinit019/qa_generator.git
)

REM Push to GitHub
echo Pushing to GitHub...
git push -u origin main
if %errorlevel% neq 0 (
    echo.
    echo If you get authentication errors:
    echo 1. Use GitHub Personal Access Token instead of password
    echo 2. Go to GitHub Settings - Developer settings - Personal access tokens
    echo 3. Generate new token with repo permissions
    echo 4. Use the token as password when prompted
    echo.
    echo Trying alternative branch name...
    git push -u origin master
    if %errorlevel% neq 0 (
        echo Error pushing to GitHub!
        echo Please check your GitHub credentials and repository access.
        pause
        exit /b 1
    )
)

echo.
echo ========================================
echo SUCCESS! Code pushed to GitHub
echo ========================================
echo.
echo Repository: https://github.com/Vinit019/qa_generator
echo.
echo Your Question Answer Generator project is now on GitHub!
echo.
pause

