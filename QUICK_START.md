# 🚀 Quick Start Guide - Question Answer Generator

## Step 1: Install Python (if not already installed)

### For Windows:
1. Go to [python.org](https://www.python.org/downloads/)
2. Download Python 3.7 or higher
3. **IMPORTANT**: Check "Add Python to PATH" during installation
4. Complete the installation

## Step 2: Set Up the Project

### Option A: Automatic Setup (Recommended)
1. **Double-click** `setup_environment.bat`
2. Wait for the setup to complete
3. **Double-click** `run_project.bat` to start the application

### Option B: Manual Setup
1. Open Command Prompt in the project folder
2. Run: `python -m venv question_generator_env`
3. Run: `call question_generator_env\Scripts\activate.bat`
4. Run: `pip install -r requirements.txt`
5. Run: `python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('averaged_perceptron_tagger')"`
6. Run: `python app.py`

## Step 3: Use the Application

1. **Open your browser**
2. **Go to**: `http://localhost:5000`
3. **Upload a document**: Drag and drop a PDF or Word file
4. **Configure settings**: Choose number of questions and difficulty
5. **Generate questions**: Click "Generate Questions"
6. **Export results**: Download as PDF or Word document

## 🎯 What You Can Do:

- **Upload Documents**: PDF, DOCX, or DOC files
- **Generate Questions**: 
  - Multiple Choice Questions (1 mark each)
  - Short Answer Questions (2 marks each)
  - Long Answer Questions (5 marks each)
- **Export Results**: Download questions as PDF or Word documents
- **Customize**: Set difficulty levels and number of questions

## 📁 Project Files:

- `setup_environment.bat` - Sets up Python environment and installs packages
- `run_project.bat` - Starts the application
- `install_python.bat` - Helps install Python if needed
- `app.py` - Main application
- `requirements.txt` - Required Python packages

## 🔧 Troubleshooting:

### Python Not Found:
- Make sure Python is installed and added to PATH
- Try running `install_python.bat` first

### Package Installation Errors:
- Check your internet connection
- Try running the setup script again

### Port Already in Use:
- Close other applications using port 5000
- Or modify `app.py` to use a different port

## 📞 Need Help?

1. Check the `INSTALLATION_GUIDE.md` for detailed instructions
2. Run `python test_app.py` to test if everything works
3. Make sure all files are in the same folder

## 🎉 Ready to Go!

Once you see "Running on http://localhost:5000" in the terminal, open your browser and start generating questions from your documents!
