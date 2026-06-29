import os
from pathlib import Path


class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-development-secret-key')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_DEFAULT_SENDER = 'noreply.zwipionline@gmail.com'

    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() in ('true', '1', 't')
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', '*')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False

    @staticmethod
    def get_db_url():
        url = os.environ.get('DATABASE_URL', 'sqlite:///' + str(Path(__file__).parent / 'zwipiOnline.db'))
        if url.startswith('postgres://'):
            url = url.replace('postgres://', 'postgresql://', 1)
        return url

    SQLALCHEMY_DATABASE_URI = get_db_url.__func__()
