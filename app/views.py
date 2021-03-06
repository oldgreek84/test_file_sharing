import datetime
import os
import uuid

from flask import (
        url_for, render_template, redirect, request, send_from_directory,
        safe_join, abort, flash
        )
from werkzeug.utils import secure_filename

from app import app, db
from app.forms import FileForm
from app.models import UploadedFile
from app.tasks import clear_old


@app.errorhandler(413)
def request_entity_too_large(error):
    return 'File Too Large', 413


@app.route('/', methods=['POST', 'GET'])
def index():
    ''' func show page this form to send file '''

    form = FileForm()
    extensions = list(app.config['ALLOWED_EXTENSIONS'])
    if form.validate_on_submit():
        file = request.files['file']
        days_count = request.form['days_count']
        now = datetime.datetime.now()
        life_date = now + datetime.timedelta(days=int(days_count))
        filename = str(uuid.uuid4()) + '-' + secure_filename(file.filename)
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

            try:
                if not os.path.exists(app.config['UPLOAD_FOLDER']):
                    os.makedirs(app.config['UPLOAD_FOLDER'])
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            except:
                flash('not save file on server')
        except:
            flash('not save in db')
            print('not saved file')
        clear_old.apply_async(args=[uploaded_file.id],
                eta=datetime.datetime.utcfromtimestamp(
                    datetime.datetime.timestamp(life_date)))
        return redirect(url_for('uploaded_files', filename=filename))
    return render_template('index.html', title='Main Page',
            form=form, extensions=extensions)


@app.route('/uploads/<path:filename>')
def uploaded_files(filename):
    ''' func show page with file data '''

    file = UploadedFile.query.filter_by(name=filename).first_or_404()
    return render_template('uploaded.html', file=file, title='Link to upload') 


@app.route('/files/<filename>')
def get_file(filename):
    ''' func return safely link to download file '''

    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/all')
def all_files():
    files = UploadedFile.query.all()
    return render_template('all_files.html', files=files)
