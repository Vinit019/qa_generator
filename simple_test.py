#!/usr/bin/env python3
"""
Simple test to check if the application can start
"""

import sys
import os

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    
    try:
        import flask
        print("[OK] Flask imported successfully")
    except ImportError as e:
        print(f"❌ Flask import failed: {e}")
        return False
    
    try:
        from document_processor import DocumentProcessor
        print("[OK] DocumentProcessor imported successfully")
    except ImportError as e:
        print(f"❌ DocumentProcessor import failed: {e}")
        return False
    
    try:
        from question_generator import QuestionGenerator
        print("[OK] QuestionGenerator imported successfully")
    except ImportError as e:
        print(f"❌ QuestionGenerator import failed: {e}")
        return False
    
    try:
        from export_utils import export_to_pdf, export_to_docx
        print("[OK] Export utilities imported successfully")
    except ImportError as e:
        print(f"❌ Export utilities import failed: {e}")
        return False
    
    return True

def test_app_creation():
    """Test if the Flask app can be created"""
    print("\nTesting Flask app creation...")
    
    try:
        from app import app
        print("[OK] Flask app created successfully")
        return True
    except Exception as e:
        print(f"❌ Flask app creation failed: {e}")
        return False

def main():
    """Main test function"""
    print("=" * 50)
    print("Question Answer Generator - Simple Test")
    print("=" * 50)
    
    # Test imports
    if not test_imports():
        print("\n❌ Import tests failed!")
        return
    
    # Test app creation
    if not test_app_creation():
        print("\n❌ App creation failed!")
        return
    
    print("\n🎉 All tests passed!")
    print("\nTo start the application:")
    print("1. Open Command Prompt in this folder")
    print("2. Run: call question_generator_env\\Scripts\\activate.bat")
    print("3. Run: python app.py")
    print("4. Open browser: http://localhost:5000")

if __name__ == "__main__":
    main()
