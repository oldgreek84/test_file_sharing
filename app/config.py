import os


base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'some-new-secret-key'

    # settings for upload file
    UPLOAD_FOLDER = base_dir + '/static/uploads/'
    # UPLOAD_FOLDER = '/static/uploads/'
    ALLOWED_EXTENSIONS = set(
            ['.jpeg', '.jpg', '.pdf', '.txt', '.docx', '.png', '.gif', 'fb2'])
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024
