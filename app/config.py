import os


base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'some-new-secret-key'

    # db config
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
            'sqlite:///' + os.path.join(base_dir, 'app.db')

    # settings for upload file
    UPLOAD_FOLDER = base_dir + '/static/uploads/'
    ALLOWED_EXTENSIONS = set(
            ['.jpeg', '.jpg', '.pdf', '.txt', '.docx', '.png', '.gif'])
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024
