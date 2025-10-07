#!/usr/bin/env python3
"""
Setup script for Question Answer Generator
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ All packages installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error installing packages: {e}")
        return False

def download_nltk_data():
    """Download required NLTK data"""
    print("Downloading NLTK data...")
    
    try:
        import nltk
        
        # Download required NLTK data
        nltk_data = [
            'punkt',
            'stopwords', 
            'averaged_perceptron_tagger'
        ]
        
        for data in nltk_data:
            try:
                nltk.data.find(f'tokenizers/{data}')
            except LookupError:
                nltk.download(data)
                print(f"✓ Downloaded {data}")
        
        print("✓ NLTK data downloaded successfully")
        return True
        
    except Exception as e:
        print(f"✗ Error downloading NLTK data: {e}")
        return False

def create_directories():
    """Create necessary directories"""
    print("Creating directories...")
    
    directories = ['uploads', 'outputs', 'templates', 'static']
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"✓ Created {directory} directory")
        else:
            print(f"✓ {directory} directory already exists")

def main():
    """Main setup function"""
    print("=" * 50)
    print("Question Answer Generator - Setup")
    print("=" * 50)
    
    # Create directories
    create_directories()
    print()
    
    # Install requirements
    if install_requirements():
        print()
        
        # Download NLTK data
        if download_nltk_data():
            print()
            print("=" * 50)
            print("✓ Setup completed successfully!")
            print("=" * 50)
            print("\nTo start the application, run:")
            print("python app.py")
            print("\nThen open your browser and go to: http://localhost:5000")
        else:
            print("✗ Setup failed at NLTK data download")
    else:
        print("✗ Setup failed at package installation")

if __name__ == "__main__":
    main()
