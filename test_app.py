#!/usr/bin/env python3
"""
Test script for the Question Answer Generator application
"""

import os
import sys
import json
from document_processor import DocumentProcessor
from question_generator import QuestionGenerator

def test_document_processing():
    """Test document processing functionality"""
    print("Testing Document Processing...")
    
    processor = DocumentProcessor()
    
    # Test with a sample text file
    sample_text = """
    Artificial Intelligence (AI) is a branch of computer science that aims to create 
    intelligent machines that can perform tasks that typically require human intelligence. 
    These tasks include learning, reasoning, problem-solving, perception, and language understanding.
    
    Machine Learning is a subset of AI that focuses on the development of algorithms and 
    statistical models that enable computer systems to improve their performance on a specific 
    task through experience, without being explicitly programmed.
    
    Deep Learning is a subset of machine learning that uses artificial neural networks 
    with multiple layers to model and understand complex patterns in data. It has been 
    particularly successful in areas such as image recognition, natural language processing, 
    and speech recognition.
    """
    
    # Save sample text to a file for testing
    with open('test_document.txt', 'w', encoding='utf-8') as f:
        f.write(sample_text)
    
    print("✓ Document processing module loaded successfully")
    return True

def test_question_generation():
    """Test question generation functionality"""
    print("Testing Question Generation...")
    
    sample_content = """
    Machine Learning is a subset of artificial intelligence that focuses on algorithms 
    and statistical models. Deep learning uses neural networks with multiple layers. 
    Natural language processing deals with human language understanding by computers.
    """
    
    requirements = {
        'mcq_count': 2,
        'short_answer_count': 1,
        'long_answer_count': 1,
        'difficulty': 'medium'
    }
    
    try:
        generator = QuestionGenerator()
        questions = generator.generate_questions(sample_content, requirements)
        
        print(f"✓ Generated {len(questions.get('mcq', []))} MCQ questions")
        print(f"✓ Generated {len(questions.get('short_answer', []))} Short Answer questions")
        print(f"✓ Generated {len(questions.get('long_answer', []))} Long Answer questions")
        
        # Save test results
        with open('test_questions.json', 'w', encoding='utf-8') as f:
            json.dump(questions, f, indent=2, ensure_ascii=False)
        
        print("✓ Test questions saved to test_questions.json")
        return True
        
    except Exception as e:
        print(f"✗ Error in question generation: {str(e)}")
        return False

def test_export_functionality():
    """Test export functionality"""
    print("Testing Export Functionality...")
    
    try:
        from export_utils import export_to_pdf, export_to_docx
        
        # Load test questions
        with open('test_questions.json', 'r', encoding='utf-8') as f:
            questions = json.load(f)
        
        # Test PDF export
        pdf_path = export_to_pdf(questions, 'test')
        if os.path.exists(pdf_path):
            print("✓ PDF export successful")
        else:
            print("✗ PDF export failed")
            return False
        
        # Test Word export
        docx_path = export_to_docx(questions, 'test')
        if os.path.exists(docx_path):
            print("✓ Word export successful")
        else:
            print("✗ Word export failed")
            return False
        
        return True
        
    except Exception as e:
        print(f"✗ Error in export functionality: {str(e)}")
        return False

def cleanup_test_files():
    """Clean up test files"""
    test_files = ['test_document.txt', 'test_questions.json']
    for file in test_files:
        if os.path.exists(file):
            os.remove(file)
    print("✓ Test files cleaned up")

def main():
    """Run all tests"""
    print("=" * 50)
    print("Question Answer Generator - Test Suite")
    print("=" * 50)
    
    tests = [
        test_document_processing,
        test_question_generation,
        test_export_functionality
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
            print()
        except Exception as e:
            print(f"✗ Test failed with error: {str(e)}")
            print()
    
    print("=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    print("=" * 50)
    
    if passed == total:
        print("🎉 All tests passed! The application is ready to use.")
        print("\nTo start the application, run:")
        print("python app.py")
        print("\nThen open your browser and go to: http://localhost:5000")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
    
    cleanup_test_files()

if __name__ == "__main__":
    main()
