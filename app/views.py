import os

from flask import (
        url_for, render_template, redirect, request, send_from_directory,
        safe_join, abort
        )
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge, BadRequestKeyError
from app import app

@app.errorhandler(413)
def request_entity_too_large(error):
    return 'File Too Large', 413

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['ALLOWED_EXTENSIONS']:
            abort(401)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_files', filename=filename))
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', title='Main Page', files=files)

@app.route('/uploads/<path:filename>')
def uploaded_files(filename):
    return render_template('uploaded.html', link=filename, title='Link to upload') 

@app.route('/files/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


