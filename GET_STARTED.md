# 🎯 Get Started with Question Answer Generator

## Current Status: Python Not Installed

The setup script detected that Python is not installed on your system. Here's how to get everything running:

## 📥 Step 1: Install Python

### For Windows (Your System):
1. **Go to**: https://www.python.org/downloads/
2. **Download**: Python 3.7 or higher (latest version recommended)
3. **Run the installer**
4. **IMPORTANT**: ✅ Check "Add Python to PATH" during installation
5. **Complete installation** and restart your computer

### Alternative: Microsoft Store
1. Open Microsoft Store
2. Search for "Python"
3. Install "Python 3.11" or latest version
4. This automatically adds Python to PATH

## 🚀 Step 2: Set Up the Project

After installing Python:

### Option A: Easy Setup (Recommended)
1. **Double-click** `setup_environment.bat`
2. Wait for automatic setup to complete
3. **Double-click** `run_project.bat` to start

### Option B: Manual Setup
1. Open Command Prompt in this folder
2. Run: `python -m venv question_generator_env`
3. Run: `call question_generator_env\Scripts\activate.bat`
4. Run: `pip install -r requirements.txt`
5. Run: `python app.py`

## 🎉 Step 3: Use the Application

1. **Open browser**: Go to `http://localhost:5000`
2. **Upload document**: Drag and drop PDF or Word file
3. **Configure**: Set number of questions and difficulty
4. **Generate**: Click "Generate Questions"
5. **Export**: Download as PDF or Word document

## 📋 What You'll Get:

- **Multiple Choice Questions (1 mark each)**
- **Short Answer Questions (2 marks each)**
- **Long Answer Questions (5 marks each)**
- **Export to PDF or Word documents**
- **Modern web interface with drag-and-drop**

## 🔧 Files Created for You:

- `setup_environment.bat` - Automatic environment setup
- `run_project.bat` - Start the application
- `install_python.bat` - Python installation helper
- `QUICK_START.md` - Quick reference guide
- `INSTALLATION_GUIDE.md` - Detailed installation guide

## ⚡ Quick Commands:

After Python is installed, you can run:

```bash
# Setup (run once)
.\setup_environment.bat

# Start application (run every time)
.\run_project.bat
```

## 🆘 Need Help?

1. **Python Installation Issues**: Check `install_python.bat`
2. **Setup Problems**: Read `INSTALLATION_GUIDE.md`
3. **Quick Reference**: Check `QUICK_START.md`
4. **Test Everything**: Run `python test_app.py` after setup

## 🎯 Next Steps:

1. **Install Python** (follow Step 1 above)
2. **Restart your computer** (important!)
3. **Run setup**: Double-click `setup_environment.bat`
4. **Start app**: Double-click `run_project.bat`
5. **Open browser**: Go to `http://localhost:5000`

The project is ready to go once Python is installed! 🚀
