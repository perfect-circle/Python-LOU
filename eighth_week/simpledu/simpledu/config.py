class BaseConfig(object):
    """ Confiig Base Class """
    SECRET_KEY = "makesur to set a very secret key"

class DevelopmentConfig(BaseConfig):
    """ Development Environment Config """
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = \
'mysql+mysqldb://root:123@147.104.245.220:3306/simpledu'

class ProductionConfig(BaseConfig):
    """ Production environment config """
    pass

class TestingConfig(BaseConfig):
    """Test environment config """
    pass

configs = {
        'development':DevelopmentConfig,
        'production':ProductionConfig,
        'testing':TestingConfig
        }
