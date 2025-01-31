import os

basedir = os.path.abspath(os.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'hospital_cardless_system.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False