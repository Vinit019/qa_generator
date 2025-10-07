<<<<<<< HEAD
# Question Answer Generator

A powerful web application that automatically generates questions from uploaded documents (PDF and Word files). The system creates different types of questions including Multiple Choice Questions (MCQ), Short Answer Questions, and Long Answer Questions based on the document content.

## Features

- **Document Processing**: Supports PDF and Word documents (.pdf, .docx, .doc)
- **Multiple Question Types**:
  - Multiple Choice Questions (1 mark each)
  - Short Answer Questions (2 marks each) 
  - Long Answer Questions (5 marks each)
- **Customizable Generation**: Configure number of questions and difficulty level
- **Export Options**: Export generated questions as PDF or Word documents
- **Modern Web Interface**: Responsive design with drag-and-drop file upload
- **Intelligent Content Analysis**: Uses NLP techniques to extract key concepts and generate relevant questions

## Installation

1. **Clone or download the project files**

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download NLTK data** (if not already downloaded):
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   nltk.download('averaged_perceptron_tagger')
   ```

## Usage

1. **Start the application**:
   ```bash
   python app.py
   ```

2. **Open your web browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **Upload a document**:
   - Drag and drop a PDF or Word file onto the upload area
   - Or click "Choose File" to browse and select a file

4. **Configure question generation**:
   - Set the number of MCQ questions (1 mark each)
   - Set the number of Short Answer questions (2 marks each)
   - Set the number of Long Answer questions (5 marks each)
   - Choose difficulty level (Easy, Medium, Hard)

5. **Generate questions**:
   - Click "Generate Questions" button
   - Wait for the system to process your document
   - View the generated questions on the web interface

6. **Export questions**:
   - Click "Export as PDF" to download questions as PDF
   - Click "Export as Word" to download questions as Word document

## Project Structure

```
question-generator/
├── app.py                 # Main Flask application
├── document_processor.py  # Document text extraction
├── question_generator.py  # Question generation logic
├── export_utils.py        # PDF/Word export functionality
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html         # Web interface
├── static/
│   └── style.css          # Custom styles
├── uploads/               # Uploaded files storage
└── outputs/               # Generated files storage
```

## Technical Details

### Document Processing
- **PDF**: Uses PyPDF2 library for text extraction
- **Word**: Uses python-docx library for document processing
- **Text Cleaning**: Removes extra whitespace, special characters, and normalizes content

### Question Generation
- **NLP Processing**: Uses NLTK for text tokenization, POS tagging, and stopword removal
- **Key Term Extraction**: Identifies important concepts and terms from the document
- **Question Types**:
  - **MCQ**: Generates multiple choice questions with correct answers and distractors
  - **Short Answer**: Creates 2-mark questions with sample answers
  - **Long Answer**: Generates 5-mark questions with detailed sample answers

### Export Functionality
- **PDF Export**: Uses ReportLab for PDF generation with formatted questions
- **Word Export**: Uses python-docx for Word document creation
- **Formatted Output**: Questions are properly formatted with options, answers, and mark allocations

## Configuration

The application can be configured by modifying the following parameters in `app.py`:

- `MAX_CONTENT_LENGTH`: Maximum file size (default: 16MB)
- `UPLOAD_FOLDER`: Directory for uploaded files
- `OUTPUT_FOLDER`: Directory for generated files

## Requirements

- Python 3.7+
- Flask 2.3.3
- PyPDF2 3.0.1
- python-docx 0.8.11
- NLTK 3.8.1
- ReportLab 4.0.7
- Bootstrap 5.1.3 (CDN)

## Troubleshooting

1. **File Upload Issues**:
   - Ensure file size is under 16MB
   - Check file format (only .pdf, .docx, .doc supported)
   - Verify file is not corrupted

2. **Question Generation Issues**:
   - Ensure document contains sufficient text content
   - Try with a different document if questions are not generated
   - Check console for error messages

3. **Export Issues**:
   - Ensure output directory has write permissions
   - Check if generated questions exist before exporting

## Future Enhancements

- Support for more document formats (PPTX, TXT)
- Advanced question generation using AI/ML models
- Question difficulty assessment
- Bulk document processing
- Question bank management
- Integration with learning management systems

## License

This project is open source and available under the MIT License.
=======
# qa_generator
>>>>>>> origin/main
