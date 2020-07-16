import datetime
import os

from flask import (
        url_for, render_template, redirect, request, send_from_directory,
        safe_join, abort
        )
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge, BadRequestKeyError

from app import app, db
from app.forms import FileForm
from app.models import UploadedFile

@app.errorhandler(413)
def request_entity_too_large(error):
    return 'File Too Large', 413

@app.route('/', methods=['POST', 'GET'])
def index():
    form = FileForm()
    if form.validate_on_submit():

        file = request.files['file']
        time = request.form['life_time']
        now = datetime.datetime.now()
        life_date = now + datetime.timedelta(minutes=int(time))
        filename = str(now.microsecond) + secure_filename(file.filename)
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['ALLOWED_EXTENSIONS']:
            abort(400)
        try:
            uploaded_file = UploadedFile(
                    name=filename,
                    link=os.path.join(app.config['UPLOAD_FOLDER'], filename),
                    life_time=life_date)
            db.session.add(uploaded_file)
            db.session.commit()
        except:
            abort(404)
            print('not work')
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_files', filename=filename))
    return render_template('index.html', title='Main Page',
            form=form)

@app.route('/uploads/<path:filename>')
def uploaded_files(filename):
    file = UploadedFile.query.filter_by(name=filename).first_or_404()
    return render_template('uploaded.html', file=file, title='Link to upload') 

@app.route('/files/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/all')
def all_files():
    files = UploadedFile.query.all()
    return render_template('all_files.html', files=files)

def clear_old(id):
    file = UploadedFile.query.get(id)
    die_time = file.life_time
    now = datetime.datetime.now()
    if now > die_time:
        db.session.delete(file)
        db.session.commit()
        try:
            os.remove(file.link)
            print('it is ok')
        except FileNotFoundError:
            print('file not exist')
    else:
        print('time to delete: ', die_time)
        print('not now')

