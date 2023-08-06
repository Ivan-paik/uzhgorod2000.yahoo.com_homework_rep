import os

class AppConfig:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = os.getenv('DEBUG')
    HOST = os.getenv('HOST')
    PORT = os.getenv('PORT')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', os.getenv('DBPARAM'))
