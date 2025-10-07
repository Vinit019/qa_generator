from flask import Flask, render_template, request, jsonify, send_file
import os
import json
from werkzeug.utils import secure_filename
from document_processor import DocumentProcessor
from question_generator import QuestionGenerator
import tempfile
import zipfile
from io import BytesIO

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'outputs'

# Ensure directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'pdf', 'docx', 'doc'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Get question requirements from form
        requirements = {
            'mcq_count': int(request.form.get('mcq_count', 5)),
            'short_answer_count': int(request.form.get('short_answer_count', 3)),
            'long_answer_count': int(request.form.get('long_answer_count', 2)),
            'difficulty': request.form.get('difficulty', 'medium')
        }
        
        try:
            # Process document
            processor = DocumentProcessor()
            content = processor.extract_text(filepath)
            
            # Generate questions
            generator = QuestionGenerator()
            questions = generator.generate_questions(content, requirements)
            
            # Save questions to file
            output_filename = f"questions_{filename.rsplit('.', 1)[0]}.json"
            output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(questions, f, indent=2, ensure_ascii=False)
            
            return jsonify({
                'success': True,
                'questions': questions,
                'download_url': f'/download/{output_filename}'
            })
            
        except Exception as e:
            return jsonify({'error': f'Error processing file: {str(e)}'}), 500
    
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(app.config['OUTPUT_FOLDER'], filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    return jsonify({'error': 'File not found'}), 404

@app.route('/export/<filename>')
def export_questions(filename):
    file_path = os.path.join(app.config['OUTPUT_FOLDER'], filename)
    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404
    
    with open(file_path, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    export_format = request.args.get('format', 'pdf')
    
    if export_format == 'pdf':
        from export_utils import export_to_pdf
        pdf_path = export_to_pdf(questions, filename)
        return send_file(pdf_path, as_attachment=True, download_name=f"questions_{filename}.pdf")
    elif export_format == 'docx':
        from export_utils import export_to_docx
        docx_path = export_to_docx(questions, filename)
        return send_file(docx_path, as_attachment=True, download_name=f"questions_{filename}.docx")
    
    return jsonify({'error': 'Invalid export format'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
