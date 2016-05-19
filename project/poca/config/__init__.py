import os
#from dotenv import load_dotenv

#dotenv_path = os.path.join(os.path.dirname(__file__), '../../..', '.env')
#load_dotenv(dotenv_path)

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('POCA_SQLALCHEMY_URL',
            'postgresql://poca_dev:pass@localhost/poca_dev')

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True


def get_test_details():
    """ If the tests are running on semaphore, then the username/password is important """
    uname = os.environ.get('DATABASE_POSTGRESQL_USERNAME')
    pw = os.environ.get('DATABASE_POSTGRESQL_PASSWORD')
    if uname and pw:
        return "{uname}:{pw}".format(uname=uname, pw=pw)
    return "poca_dev:pass"

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI ='postgresql://{0}@localhost/poca_test'.format(get_test_details())

