# Installation Guide - Question Answer Generator

## Prerequisites

Before installing the Question Answer Generator, you need to have Python installed on your system.

### Installing Python (if not already installed)

#### For Windows:
1. Go to [python.org](https://www.python.org/downloads/)
2. Download the latest Python version (3.7 or higher)
3. Run the installer and **make sure to check "Add Python to PATH"**
4. Verify installation by opening Command Prompt and typing: `python --version`

#### For macOS:
1. Install Homebrew if you don't have it: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
2. Install Python: `brew install python`

#### For Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3 python3-pip
```

## Installation Steps

### 1. Download/Clone the Project
- Download all project files to a folder on your computer
- Or clone the repository if using Git

### 2. Open Terminal/Command Prompt
- Navigate to the project folder
- On Windows: Open Command Prompt or PowerShell
- On macOS/Linux: Open Terminal

### 3. Install Dependencies

#### Option A: Automatic Setup (Recommended)
```bash
python setup.py
```

#### Option B: Manual Installation
```bash
# Install required packages
pip install -r requirements.txt

# Download NLTK data
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('averaged_perceptron_tagger')"
```

### 4. Run the Application
```bash
python app.py
```

### 5. Access the Application
- Open your web browser
- Go to: `http://localhost:5000`
- The application should now be running!

## Troubleshooting

### Python Not Found Error
If you get "Python was not found" error:
1. Make sure Python is installed
2. Try using `python3` instead of `python`
3. On Windows, try using `py` command
4. Add Python to your system PATH

### Package Installation Errors
If you get errors installing packages:
1. Update pip: `python -m pip install --upgrade pip`
2. Try installing packages individually
3. Use virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   pip install -r requirements.txt
   ```

### NLTK Data Download Issues
If NLTK data download fails:
1. Check internet connection
2. Try downloading manually:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   nltk.download('averaged_perceptron_tagger')
   ```

### Port Already in Use
If port 5000 is already in use:
1. Stop other applications using port 5000
2. Or modify `app.py` to use a different port:
   ```python
   app.run(debug=True, host='0.0.0.0', port=5001)  # Change port to 5001
   ```

## Testing the Installation

Run the test script to verify everything is working:
```bash
python test_app.py
```

This will test:
- Document processing
- Question generation
- Export functionality

## File Structure After Installation

```
question-generator/
├── app.py                 # Main application
├── document_processor.py  # Document processing
├── question_generator.py  # Question generation
├── export_utils.py        # Export functionality
├── setup.py              # Setup script
├── test_app.py           # Test script
├── requirements.txt      # Dependencies
├── templates/            # Web templates
├── static/               # CSS/JS files
├── uploads/              # Uploaded files
└── outputs/              # Generated files
```

## Usage

1. **Start the application**: `python app.py`
2. **Open browser**: Go to `http://localhost:5000`
3. **Upload document**: Drag and drop a PDF or Word file
4. **Configure settings**: Set number of questions and difficulty
5. **Generate questions**: Click "Generate Questions"
6. **Export results**: Download as PDF or Word document

## Support

If you encounter any issues:
1. Check the error messages in the terminal
2. Ensure all dependencies are installed
3. Verify Python version (3.7+ required)
4. Check file permissions for uploads and outputs directories

## System Requirements

- **Python**: 3.7 or higher
- **RAM**: 2GB minimum, 4GB recommended
- **Storage**: 100MB for application + space for documents
- **OS**: Windows 10+, macOS 10.14+, or Linux
- **Browser**: Modern browser (Chrome, Firefox, Safari, Edge)
