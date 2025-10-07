# 🚀 Git Setup Guide - Push to GitHub Repository

## Step 1: Install Git

### For Windows:
1. **Download Git**: Go to https://git-scm.com/download/win
2. **Install Git**: Run the installer with default settings
3. **Restart Command Prompt/PowerShell** after installation
4. **Verify Installation**: Run `git --version` in Command Prompt

### Alternative: GitHub Desktop
1. **Download**: https://desktop.github.com/
2. **Install**: GitHub Desktop (includes Git)
3. **Sign in** with your GitHub account

## Step 2: Configure Git (First Time Only)

Open Command Prompt and run:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Step 3: Push Code to Repository

### Option A: Using Command Prompt (Recommended)

1. **Open Command Prompt** in the project folder
2. **Initialize Git repository**:
   ```bash
   git init
   ```

3. **Add all files**:
   ```bash
   git add .
   ```

4. **Commit files**:
   ```bash
   git commit -m "Initial commit: Question Answer Generator"
   ```

5. **Add remote repository**:
   ```bash
   git remote add origin https://github.com/Vinit019/qa_generator.git
   ```

6. **Push to GitHub**:
   ```bash
   git push -u origin main
   ```

### Option B: Using GitHub Desktop

1. **Open GitHub Desktop**
2. **File → Clone Repository**
3. **URL**: `https://github.com/Vinit019/qa_generator.git`
4. **Clone** the repository
5. **Copy all project files** to the cloned folder
6. **Commit & Push** using GitHub Desktop interface

## Step 4: Verify Upload

1. **Go to**: https://github.com/Vinit019/qa_generator
2. **Check** if all files are uploaded
3. **Files should include**:
   - `app.py`
   - `document_processor.py`
   - `question_generator.py`
   - `export_utils.py`
   - `requirements.txt`
   - `README.md`
   - `templates/`
   - `static/`
   - All batch files

## 🔧 Troubleshooting

### Git Not Found Error:
- Install Git from https://git-scm.com/download/win
- Restart Command Prompt after installation

### Authentication Issues:
- Use GitHub Personal Access Token instead of password
- Go to GitHub Settings → Developer settings → Personal access tokens
- Generate new token with repo permissions

### Repository Access Issues:
- Make sure you have write access to the repository
- Check if the repository URL is correct
- Verify your GitHub credentials

## 📁 Files to Upload

The following files will be pushed to the repository:

### Core Application:
- `app.py` - Main Flask application
- `document_processor.py` - Document processing
- `question_generator.py` - Question generation
- `export_utils.py` - Export functionality

### Configuration:
- `requirements.txt` - Python dependencies
- `README.md` - Project documentation
- `INSTALLATION_GUIDE.md` - Installation guide
- `QUICK_START.md` - Quick start guide
- `GET_STARTED.md` - Getting started guide

### Setup Scripts:
- `setup_environment.bat` - Environment setup
- `run_project.bat` - Run application
- `install_python.bat` - Python installation helper

### Web Interface:
- `templates/index.html` - Web interface
- `static/style.css` - Custom styles

### Test Files:
- `test_app.py` - Comprehensive tests
- `simple_test.py` - Simple tests
- `test_server.py` - Server tests

## 🎯 After Upload

Once the code is uploaded to GitHub:

1. **Update README.md** with project description
2. **Add topics/tags** to the repository
3. **Create releases** for version management
4. **Set up GitHub Pages** for documentation (optional)

## 📞 Need Help?

If you encounter issues:
1. **Check Git installation**: `git --version`
2. **Verify repository access**: Make sure you can access the GitHub repo
3. **Check file permissions**: Ensure all files are in the correct folder
4. **Use GitHub Desktop**: Easier alternative to command line

The project is ready to be pushed to GitHub! 🚀

