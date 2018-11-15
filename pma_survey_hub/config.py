"""Application configuration classes."""
import platform
import os


basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
settings = {
    'App Icon': '',
    'App Short-Title': 'Survey Hub',
    'App Title': 'PMA Survey Hub',
    'Secret Key': '',
    'Toggle Placeholders': False
}


def get_settings(setting=''):
    """Settings"""
    if not setting:
        return settings
    else:
        return settings[setting]


def temp_folder_path():
    """Get the path to temp upload folder."""
    if platform.system() == 'Windows':
        return basedir + '\\temp'
    return basedir + '/temp/'


class Config:
    """Base configuration."""
    TESTING = False
    CSRF_ENABLED = True
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class StagingConfig(Config):
    """Production configuration."""
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class ProductionConfig(Config):
    """Production configuration."""
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLITE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.db')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', SQLITE_URI)


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'staging': StagingConfig,
    # And the default is...
    'default': DevelopmentConfig
}
