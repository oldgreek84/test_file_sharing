import os


base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    ''' class set settings for app '''

    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'some-new-secret-key'

    # db config
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
            'sqlite:///' + os.path.join(base_dir, 'app.db')

    # settings for upload file
    UPLOAD_FOLDER = base_dir + '/static/uploads/'
    ALLOWED_EXTENSIONS = set(
            ['.jpeg', '.jpg', '.pdf', '.txt', '.docx', '.png', '.gif', '.fb2'])
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024

    # settings for redis
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

